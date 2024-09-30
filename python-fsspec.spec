# Avoid dependency loops:
#     fsspec -> distributed -> dask -> fsspec
#     fsspec -> gcsfs -> fsspec
#     fsspec -> zarr -> fsspec
%bcond bootstrap 0

%global srcname fsspec

Name:           python-%{srcname}
Version:        2024.6.1
%global tag     2024.6.1
Release:        %autorelease
Summary:        Specification for Pythonic file system interfaces

License:        BSD-3-Clause
URL:            https://github.com/fsspec/filesystem_spec
Source0:        %{url}/archive/%{tag}/%{srcname}-%{tag}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(pytest-mock)
BuildRequires:  python3dist(pytest-vcr)
BuildRequires:  python3dist(cloudpickle)
%if %{without bootstrap}
#BuildRequires:  python3dist(distributed) -- not yet available in Fedora
BuildRequires:  python3dist(zarr)
%endif
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(lz4)
BuildRequires:  python3dist(notebook)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(python-snappy)
BuildRequires:  python3dist(zstandard)
BuildRequires:  git-core

%global _description %{expand:
Filesystem Spec is a project to unify various projects and classes to work with
remote filesystems and file-system-like abstractions using a standard pythonic
interface.}

%description %{_description}


%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n filesystem_spec-%{tag} -p1

%generate_buildrequires
# Skipped extras:
# - (when bootstrapping) gcs and gs: Don't have gcsfs
# - abfs and adl: Don't have adlfs
# - arrow and hdfs: Don't have pyarrow
# - dropbox: Don't have dropboxdrivefs
# - fuse: Won't work in a build since it requires the kernel module to be loaded.
# - gui: Don't have panel
# - oci: Don't have ocifs
# - s3: Don't have s3fs
# - sftp and ssh: Requires a running SSH server in a container
# - smb: Requires a running SMB server in a container.
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires -x %{?!with_bootstrap:dask,gcs,gs,}git,github,http,libarchive,tqdm

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%{pytest} -vra

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
