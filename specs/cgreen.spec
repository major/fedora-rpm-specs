Name:           cgreen
Version:        1.6.3
Release:        %autorelease
Summary:        Modern unit test and mocking framework for C and C++
License:        ISC
URL:            https://github.com/cgreen-devs/%{name}
Source0:        https://github.com/cgreen-devs/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

# https://bugzilla.redhat.com/show_bug.cgi?id=2068898
ExcludeArch: s390x

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  perl-interpreter
BuildRequires:  asciidoctor

%description
A modern, portable, cross-language unit testing and mocking framework for C
and C++.


%package devel
Summary:        Libraries and headers for developing programs with Cgreen
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Libraries and headers for developing programs with Cgreen.


%package runner
Summary:        A runner for the Cgreen unit testing and mocking framework
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description runner
A runner for the Cgreen unit testing and mocking framework.


%prep
%autosetup -p1

%build
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake -DCGREEN_WITH_HTML_DOCS=ON
%cmake_build

%install
%cmake_install

%check
%ifarch i686
/usr/bin/ctest --test-dir redhat-linux-build --output-on-failure \
    --force-new-ctest-process -j8 \
    --exclude-regex "assertion_messages"
%else
/usr/bin/ctest --test-dir redhat-linux-build --output-on-failure \
    --force-new-ctest-process -j8
%endif

%files
%license LICENSE
%doc README.md
%{_libdir}/libcgreen.so.1*


%files devel
%doc doc/cgreen-guide-en-docinfo.html
%{_libdir}/libcgreen.so
%{_includedir}/cgreen
%{_libdir}/cmake/cgreen


%files runner
%{_bindir}/cgreen-debug
%{_bindir}/cgreen-runner
%{_mandir}/man1/cgreen-runner.1*
%{_mandir}/man1/cgreen-debug.1*
%{_mandir}/man5/cgreen.5*
%{_datadir}/bash-completion/completions/cgreen-debug
%{_datadir}/bash-completion/completions/cgreen-runner


%changelog
%autochangelog
