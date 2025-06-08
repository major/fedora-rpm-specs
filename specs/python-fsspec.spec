%global _with_bootstrap 1
# Avoid dependency loops:
#     fsspec -> distributed -> dask -> fsspec
#     fsspec -> gcsfs -> fsspec
#     fsspec -> zarr -> fsspec
%bcond bootstrap 0

%global srcname fsspec

Name:           python-%{srcname}
Version:        2025.5.1
%global tag     2025.5.1
Release:        %autorelease
Summary:        Specification for Pythonic file system interfaces

License:        BSD-3-Clause
URL:            https://github.com/fsspec/filesystem_spec
Source:         %{url}/archive/%{tag}/%{srcname}-%{tag}.tar.gz
# Submitted upstream: https://github.com/fsspec/filesystem_spec/pull/1857
Patch:          Create-an-event-loop-if-it-doesn-t-exist.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(pytest-mock)
BuildRequires:  python3dist(pytest-rerunfailures)
BuildRequires:  python3dist(cloudpickle)
%if %{without bootstrap}
BuildRequires:  python3dist(zarr)
BuildRequires:  python3dist(notebook)
%endif
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(lz4)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(python-snappy)
BuildRequires:  python3dist(zstandard)
BuildRequires:  fuse
BuildRequires:  git-core

%global _description %{expand:
Filesystem Spec is a project to unify various projects and classes to work with
remote filesystems and file-system-like abstractions using a standard pythonic
interface.}

%description %{_description}


%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%pyproject_extras_subpkg -n python3-%{srcname} arrow
%pyproject_extras_subpkg -n python3-%{srcname} dask
%pyproject_extras_subpkg -n python3-%{srcname} entrypoints
%pyproject_extras_subpkg -n python3-%{srcname} fuse
%if %{without bootstrap}
%pyproject_extras_subpkg -n python3-%{srcname} gcs
%endif
%pyproject_extras_subpkg -n python3-%{srcname} git
%pyproject_extras_subpkg -n python3-%{srcname} github
%if %{without bootstrap}
%pyproject_extras_subpkg -n python3-%{srcname} gs
%endif
%pyproject_extras_subpkg -n python3-%{srcname} hdfs
%pyproject_extras_subpkg -n python3-%{srcname} http
%pyproject_extras_subpkg -n python3-%{srcname} libarchive
%pyproject_extras_subpkg -n python3-%{srcname} sftp
%pyproject_extras_subpkg -n python3-%{srcname} smb
%pyproject_extras_subpkg -n python3-%{srcname} ssh
%pyproject_extras_subpkg -n python3-%{srcname} tqdm


%prep
%autosetup -n filesystem_spec-%{tag} -p1

%generate_buildrequires
# Skipped extras:
# - (when bootstrapping) gcs and gs: Don't have gcsfs
# - abfs and adl: Don't have adlfs
# - dropbox: Don't have dropboxdrivefs
# - gui: Don't have panel
# - oci: Don't have ocifs
# - s3: Don't have s3fs
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires -x arrow,%{?!with_bootstrap:dask,gcs,gs,}entrypoints,fuse,git,github,hdfs,http,libarchive,sftp,smb,ssh,tqdm

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
# fuse tests fail on koji builders due to missing kernel modules
# test_async_cat_file_ranges uses the network; https://github.com/fsspec/filesystem_spec/pull/1734/files#r1893434370
# test_gist.py and test_github.py tests require network
%{pytest} -vra \
  --deselect=fsspec/tests/test_fuse.py::test_basic \
  --deselect=fsspec/tests/test_fuse.py::test_chmod \
  --deselect=fsspec/tests/test_fuse.py::test_seek_rw \
  --deselect=fsspec/implementations/tests/test_reference.py::test_async_cat_file_ranges \
  --ignore=fsspec/implementations/tests/test_gist.py \
  --ignore=fsspec/implementations/tests/test_github.py


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
