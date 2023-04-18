"""Module for downloading specific files from Gitlab with a personal access token stored in environment variables."""


__author__ = "Maarten de Jeu"
__copyright__ = "Copyright 2022, Hogeschool Utrecht"


from typing import Union, Callable
import os


# Hardcoded in script so that student file structure doesn't get cluttered with .env file.
_ACCESS_TOKEN_ENV_NAME: str = "AC_GITLAB_ACCESS_TOKEN"


# OS Module raises OSError according to documentation if specific functionalities are not available
# on used OS. Doesn't propagate error so that the one student that uses
# an obscure Linux-distro's workflow is not disturbed in any way.
def _catch_os_exception(f: Callable) -> Callable:
    """Function decorator that catches OSErrors during wrapped function's runtime.

    Wrapped function returns None whenever OSError is caught during runtime.
    Implemented as decorator because previous versions of module needed this for multiple functions.

    Args:
        f: function to wrap.

    Returns:
        function wrapped in try/except block that catches OSError's, which returns None if an exception gets raised."""

    def f_new(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except OSError:  # FIXME(m-jeu): Consider logging exception message on catch.
            return None

    return f_new


@_catch_os_exception
def _fetch_access_token(env_var_name: str) -> Union[str, None]:
    """Fetch a variable from either the system variables, or user variables (on Windows).

    Fetches variable through os.environ, which practically is an interface that's implemented differently for every OS.
    Consult os.environ documentation for specific OS for more information.

    Wrapped in _catch_os_exception.

    Args:
        env_var_name: name of variable in environment.

    Returns:
        Value for specified variable name if present, None if variable not present or OSException is raised."""
    return os.environ.get(env_var_name)


def _download_from_gitlab(*,
                          host: str,
                          token: str,
                          project_id: int,
                          branch_name: str,
                          file_path: str,
                          output_name: str) -> None:
    """Download a file from Gitlab using a personal-access token into the current folder.

    Args:
        host: Host to connect to.
        token: Gitlab personal access token, usually a string of characters.
        project_id: Gitlab project ID.
        branch_name: name of the branch that file can be found on.
        file_path: file path/name (with extension) of the file that should be downloaded.
        output_name: name that the downloaded file should have once downloaded (including extension).

    E.G.:
    Consider we want to download the file "brum.jpg" in the repository https://gitlab.com/m-jeu/cool-test-repo,
    and store it as "downloaded_picture.jpg". The relevant function call would be:
    _dowload_from_gitlab(
        host="https://gitlab.com",
        token="ABCDEFG",
        project_id=35523853,
        branch_name="main",
        file_path="brum.jpg",
        output_name="downloaded_picture.jpg"
    )"""

    # pip install python-gitlab
    import gitlab  # Import within function, so import doesn't happen when student is working.

    lab_connection = gitlab.Gitlab(host, private_token=token)  # Connection errors not caught because code should only
    project = lab_connection.projects.get(project_id)          # be executed when person has token set in sys variables.

    with open(output_name, "wb") as file:
        project.files.raw(
            file_path=file_path,
            ref=branch_name,
            streamed=True,
            action=file.write
        )


def download_if_token_in_env(*,
                             project_id: int,
                             file_path: str,
                             token_name_in_env: str = _ACCESS_TOKEN_ENV_NAME,
                             host: str = "https://gitlab.com",
                             branch_name: str = "main",
                             output_name: str = "gitlab_download.txt",
                             ) -> bool:
    """Download a file from Gitlab if a personal access token is present is system variables.

    Args:
        project_id: GitLab project ID.
        file_path: file path/name (with extension) of the file that should be downloaded.
        token_name_in_env: name of GitLab personal access token in system variables.
        host: host to connect to.
        branch_name: name of branch on GitLab to download file from.
        output_name: name that downloaded file should be given locally (with extension).

    Returns:
        Download success."""
    token: str = _fetch_access_token(token_name_in_env)
    if token:
        _download_from_gitlab(host=host, token=token, project_id=project_id,
                              branch_name=branch_name, file_path=file_path, output_name=output_name)
        return True
    return False
