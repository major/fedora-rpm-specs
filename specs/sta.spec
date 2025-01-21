Name: sta
Summary: Simple statistics tool for the command line
License: MIT

%global git_date 20231130
%global git_commit 94559e3dfa97d415e3f37b1180b57c17c7222b4f
%global git_sha %(c="%{git_commit}"; echo "${c:0:7}")

Version: 0^%{git_date}.%{git_sha}
Release: 3%{?dist}

URL: https://github.com/simonccarter/sta
Source0: %{URL}/archive/%{git_commit}/sta-%{git_commit}.tar.gz

# Adds a man page for the program.
# Submitted upstream: https://github.com/simonccarter/sta/pull/13/
Patch0: sta--man-page.patch

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: cxxtest
BuildRequires: gcc-c++
BuildRequires: make

%description
sta is a lightweight, fast tool for calculating basic descriptive statistics
from the command line. Inspired by "st", this project differs in that
it is written in C++, allowing for faster computation of statistics
given larger non-trivial data sets.

Additions include the choice of biased vs unbiased estimators
and the option to use the compensated variant algorithm.


%prep
%autosetup -p1 -n %{name}-%{git_commit}


%build
autoreconf -ifv
%configure
%make_build


%install
%make_install


%check
cd test/
cxxtestgen --error-printer --have-std -o tests.cpp sta_test_1.h sta_test_2.h
g++ %{optflags} %{build_ldflags} -o tester tests.cpp
./tester


%files
%doc README.md
%license LICENCE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0^20231130.94559e3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Dec 19 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0^20231130.94559e3-2
- Add a man page
- Run tests in %%check

* Thu Dec 19 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0^20231130-1
- Initial packaging
