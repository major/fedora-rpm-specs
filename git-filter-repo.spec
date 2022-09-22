%global gitexecdir %{_libexecdir}/git-core

Name:           git-filter-repo
Version:        2.34.0
Release:        4%{?dist}
Summary:        Quickly rewrite git repository history (git-filter-branch replacement)
License:        MIT
Group:          Development/Tools/Version Control
Url:            https://github.com/newren/git-filter-repo
#
Source0:        https://github.com/newren/git-filter-repo/releases/download/v%{version}/%{name}-%{version}.tar.xz
#
BuildArch:      noarch
#
BuildRequires:  git >= 2.26.0
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
#
Requires:       git >= 2.26.0

%description
git filter-repo is a versatile tool for rewriting history, which includes
capabilities not found anywhere else. It roughly falls into the same space of
tool as git filter-branch but without the capitulation-inducing poor
performance, with far more capabilities, and with a design that scales
usability-wise beyond trivial rewriting cases.

%prep
%autosetup -p1

# Change shebang in all relevant files in this directory and all subdirectories
find -type f -exec sed -i '1s=^#!%{_bindir}/\(python\|env python\)[23]\?=#!%{_bindir}/python3=' {} +

%build

%install
install -d -m 0755 %{buildroot}%{gitexecdir}
install -m 0755 git-filter-repo %{buildroot}%{gitexecdir}/git-filter-repo

install -d -m 0755 %{buildroot}%{python3_sitelib}
ln -sf %{gitexecdir}/git-filter-repo %{buildroot}%{python3_sitelib}/git_filter_repo.py

install -d -m 0755 %{buildroot}%{_mandir}/man1
install -m 0644 Documentation/man1/git-filter-repo.1 %{buildroot}%{_mandir}/man1/git-filter-repo.1

%files
%license COPYING
%doc README.md contrib/filter-repo-demos
%{gitexecdir}/git-filter-repo
%{python3_sitelib}/git_filter_repo.py
%{_mandir}/man1/git-filter-repo.1*

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.34.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.34.0-3
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.34.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 23 2021 Andreas Schneider <asn@redhat.com> - 2.34.0-1
- Update to version 2.34.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.29.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.29.0-3
- Rebuilt for Python 3.10

* Mon Mar 15 2021 Andreas Schneider <asn@redhat.com> - 0.29.0-1
- Update to version 2.29.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 06 2020 Andreas Schneider <asn@redhat.com> - 2.28.0-1
- Update to version 2.28.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.27.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 02 2020 Andreas Schneider <asn@redhat.com> - 2.27.0-1
- Update to version 2.27.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.25.0-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Andreas Schneider <asn@redhat.com> - 2.25.0-4
- Add missing BR for python3-rpm-macros

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.25.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Andreas Schneider <asn@redhat.com> - 2.25.0-1
- Update to version 2.25.0
- Fix installation to python3 sitelib

* Fri Dec 20 2019 Andreas Schneider <asn@redhat.com> - 2.24.0-2
- Fixed source tarball permissions
- Fixed souperfluous space in Summary

* Thu Dec 19 2019 Andreas Schneider <asn@redhat.com> - 2.24.0-1
- Initial version 2.24.0
