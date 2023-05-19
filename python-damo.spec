%bcond_without  check

%global srcname damo
%global _description %{expand:
damo is a user space tool for DAMON. Using this, you can monitor the data access
patterns of your system or workloads and make data access-aware memory
management optimizations.}

Name:           python-%{srcname}
Version:        1.8.1
Release:        %autorelease
Summary:        Data Access Monitoring Operator

License:        GPL-2.0-only
URL:            https://github.com/awslabs/damo
# PyPI source does not contain tests
# Source:         %%pypi_source
Source:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
# remove shebangs
Patch:         %{url}/pull/43.patch#/%{srcname}-remove_shebangs.diff

BuildArch:      noarch
# some tests assume 64-bit and fail on ix86
ExclusiveArch:  x86_64 aarch64 ppc64le s390x noarch

%description %{_description}


%package -n %{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
%if %{with check}
BuildRequires:  python3dist(pytest)
%endif

%description -n %{srcname} %{_description}


%prep
%autosetup -p 1 -n %{srcname}-%{version}


# from packaging/build.sh
for f in pyproject.toml setup.py; do
  cp -p packaging/$f .
done

mkdir -p src/damo
cp -p *.py src/damo/
cp -p damo src/damo/damo.py
touch src/damo/__init__.py

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%if %{with check}
%check
%pytest
%endif


%files -n %{srcname} -f %{pyproject_files}
%license COPYING
%doc CONTRIBUTING README.md SECURITY.md USAGE.md
%{_bindir}/%{srcname}


%changelog
%autochangelog
