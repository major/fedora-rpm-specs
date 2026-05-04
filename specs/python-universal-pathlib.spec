Name:           python-universal-pathlib
Version:        0.3.10
Release:        %autorelease
Summary:        Python pathlib API extended to use fsspec backends

License:        MIT
URL:            https://github.com/fsspec/universal_pathlib
Source:         %{pypi_source universal_pathlib}

# smbclient is unavailable and tests can't work as they use docker.
# gcsfs/s3fs are unavailable so skip a test that requires them.
Patch:          0001-Make-some-dependencies-more-optional-in-tests.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(fsspec[github])
BuildRequires:  python3dist(fsspec[http])
BuildRequires:  python3dist(fsspec[ssh])

%global _description %{expand:
Universal Pathlib is a Python library that extends the pathlib_abc.JoinablePath
API to provide a pathlib.Path-like interface for a variety of backend
filesystems via filesystem_spec.}

%description %_description

%package -n     python3-universal-pathlib
Summary:        %{summary}

%description -n python3-universal-pathlib %_description

%prep
%autosetup -p1 -n universal_pathlib-%{version}
# Don't need mypy/lint dependencies.
%pyproject_patch_dependency mypy:ignore
%pyproject_patch_dependency pylint:ignore
%pyproject_patch_dependency pytest-cov:ignore
%pyproject_patch_dependency pytest-mypy-plugins:ignore
%pyproject_patch_dependency pytest-sugar:ignore

%generate_buildrequires
%pyproject_buildrequires -x tests

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l upath

%check
%pytest -ra -m 'not network'

%files -n python3-universal-pathlib -f %{pyproject_files}
%doc README.md CHANGELOG.md

%changelog
%autochangelog
