# Increment the serial number every time we update the commit hash.
%global serial 2
%global commit 5039d9949317db76880f9075102ef9662f58531b

Name:           pythoncapi-compat
Summary:        Python C API compatibility
# Upstream has never versioned this project.
Version:        0^%{serial}.%{sub %{commit} 1 7}
Epoch:          2
Release:        %autorelease

License:        0BSD
URL:            https://github.com/python/pythoncapi-compat
Source:         %{url}/archive/%{commit}/pythoncapi-compat-%{commit}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++

# As a header-only library package, the base package is arched so that it is
# compiled and tested on all architectures; however, no compiled code is
# installed, and there are no debugging symbols.
%global debug_package %{nil}

%global common_description %{expand:
The pythoncapi-compat project can be used to write a C or C++ extension
supporting a wide range of Python versions with a single code base. It is made
of the pythoncapi_compat.h header file.}

%description %{common_description}


%package devel
Summary:        %{summary}

BuildArch:      noarch

# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_packaging_header_only_libraries
Provides:       pythoncapi-compat-static = %{epoch}:%{version}-%{release}
# We dropped the separate -doc subpackage, but the docs are still here:
Provides:       pythoncapi-compat-doc = %{epoch}:%{version}-%{release}

# Upstream removed the upgrade_pythoncapi.py script in commit
# 2682b1e65b1a8c105e22791a5f60cf462872b10f, so we had to drop the -tools
# subpackage that had contained it.
Obsoletes:      pythoncapi-compat-tools < 2:0^1.2682b1e-1
# At the same time, we merged the documentation into the -devel package. With
# only one binary package to document the reStructuredText files are not large
# or numerous enough to justify keeping a separate -doc subpackage.
Obsoletes:      pythoncapi-compat-doc < 2:0^1.2682b1e-1

%description devel %{common_description}


%prep
%autosetup -n pythoncapi-compat-%{commit}

# Compiling with -Werror makes sense for upstream CI, but is probably too
# brittle for downstream builds.
sed --regexp-extended --in-place "s/^([[:blank:]]*)(['\"]-Werror)/\1# \2/" \
    tests/setup.py


%generate_buildrequires
%pyproject_buildrequires --directory tests


%build
%pyproject_wheel --directory tests


%install
install -D --preserve-timestamps --mode=0644 \
    --target='%{buildroot}%{_includedir}' pythoncapi_compat.h


%check
%{py3_test_envvars} %{python3} runtests.py \
    --current --verbose %{?_smp_build_ncpus:--jobs %{_smp_build_ncpus}}


%files devel
%license COPYING
%doc README.rst
%doc docs/*.rst

%{_includedir}/pythoncapi_compat.h


%changelog
%autochangelog
