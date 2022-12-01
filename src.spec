Name:           src
Version:        1.29
Release:        1%{?dist}
Summary:        Simple Revision Control

License:        BSD
URL:            https://gitlab.com/esr/src
Source0:        https://gitlab.com/esr/src/-/archive/%{version}/%{name}-%{version}.tar.bz2
    
BuildRequires:  asciidoc
BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  rcs

Requires:       rcs
Requires:       python3
Recommends:     git-core

BuildArch:      noarch

%description
Simple Revision Control is RCS reloaded with a modern UI, designed to
manage single-file solo projects kept more than one to a directory.
Has a modern, svn/hg/git-like UI

%prep
%autosetup
%py3_shebang_fix src

%build
%make_build all FAQ.html

%install
%make_install prefix=%{_prefix}

%check
# We must provide a valid git user configuration for the tests to pass.
mkdir git-home
cat > git-home/.gitconfig <<'EOF'
[user]  
        name = Bogus Example
        email = bogus@example.com
EOF
# Redirecting and capturing stderr keeps the test script from detecting the
# terminal size, which affects the output and can cause failures.
result="$(HOME="${PWD}/git-home" ./srctest -b rcs -p %{python3} 2>&1)"
echo "${result}"
    
%files
%license COPYING
%doc NEWS README FAQ.html
%{_bindir}/src
%{_mandir}/man1/src.1*

%changelog
* Tue Nov 29 2022 Bob Hepple <bob.hepple@gmail.com> - 1.29-1
- new version
- remove Patch0:src-1.28-backport-1bbebb4a.patch 

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue May 04 2021 Bob Hepple <bob.hepple@gmail.com> - 1.28-2
- rebuilt

* Thu Apr 22 2021 Bob Hepple <bob.hepple@gmail.com> - 1.28-1
- rebuilt

