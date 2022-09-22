Name:           hedley
Summary:        A C/C++ header to help move #ifdefs out of your code
Version:        15
Release:        %autorelease

URL:            https://nemequ.github.io/%{name}/
Source0:        https://github.com/nemequ/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
License:        CC0

BuildRequires:  gcc-c++
BuildRequires:  make

%global common_description %{expand:
Hedley is a single C/C++ header you can include in your project to enable
compiler-specific features while retaining compatibility with all compilers. It
contains dozens of macros to help make your code easier to use, harder to
misuse, safer, faster, and more portable.

You can safely include Hedley in your public API, and it works with virtually
any C or C++ compiler.}

%description %{common_description}


%package devel
Summary:        %{summary}

Provides:       %{name}-static = %{version}-%{release}

%description devel %{common_description}


%prep
%autosetup


# No build section required for single-header library with single-header source


%install
install -d %{buildroot}%{_includedir}
install -t %{buildroot}%{_includedir} -p -m 0644 %{name}.h


%check
# As far as we can tell, the tests are intended to be used by compiling them,
# not by running the result. See .travis.yml.
%set_build_flags
%make_build -C test


%files devel
%license COPYING
%doc NEWS
%doc README.md

%{_includedir}/%{name}.h


%changelog
%autochangelog
