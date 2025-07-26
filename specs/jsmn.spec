Name: jsmn
Summary: Minimalistic JSON parser / tokenizer for C
License: MIT

%global git_date 20211014
%global git_commit 25647e692c7906b96ffd2b05ca54c097948e879c
%global git_sha %(c="%{git_commit}"; echo "${c:0:7}")

Version: 1.1.0^%{git_date}git%{git_sha}
Release: 3%{?dist}

URL: http://zserge.com/jsmn.html
Source0: https://github.com/zserge/jsmn/archive/%{git_commit}/jsmn-%{git_commit}.tar.gz

# Any debuginfo we generate along the way pertains only to tests.
%global debug_package %{nil}

BuildRequires: gcc
BuildRequires: make

# Main package is not "BuildArch: noarch"
# because we want to run the tests on all architectures.

%global desc %{expand:
jsmn (pronounced like 'jasmine') is a minimalistic JSON parser written in C.
It can be easily integrated into resource-limited or embedded projects.

Most JSON parsers offer you a bunch of functions to load JSON data, parse it
and extract any value by its name. jsmn proves that checking the correctness
of every JSON packet or allocating temporary objects to store parsed
JSON fields often is an overkill.

jsmn is designed to be robust (it should work fine even with erroneous data),
fast (it should parse data on the fly), portable (no superfluous dependencies
or non-standard C extensions). And of course, simplicity is a key feature:
simple code style, simple algorithm, simple integration into other projects.
}

%description %{desc}


%package devel
Summary: %{summary}
Provides: %{name}-static = %{version}-%{release}
BuildArch: noarch

%description devel %{desc}


%prep
%autosetup -p1 -n jsmn-%{git_commit}


%build
# Nothing to do here


%install
install -m 755 -d %{buildroot}%{_includedir}/%{name}
install -m 644 -p jsmn.h %{buildroot}%{_includedir}/%{name}/%{name}.h


%check
%make_build test


%files devel
%doc README.md
%license LICENSE
%{_includedir}/%{name}


%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0^20211014git25647e6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Mar 01 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.1.0^20211014git25647e6-2
- Run tests on all architectures
- Include README in -devel package

* Fri Feb 28 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.1.0^20211014git25647e6-1
- Initial packaging
