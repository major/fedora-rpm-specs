Name:		asciinema
Version:	2.2.0
Release:	5%{?dist}
Summary:	Terminal session recorder
License:	GPLv3+
URL:		https://asciinema.org
Source0:	https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	python3-devel
BuildRequires:	python3-pytest


%description
Asciinema is a free and open source solution for recording the terminal sessions
and sharing them on the web.


%prep
%autosetup -n %{name}-%{version}

%generate_buildrequires
%pyproject_buildrequires 


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{name}

# man page
install -d %{buildroot}%{_mandir}/man1
install -p -m 644 man/asciinema.1 %{buildroot}%{_mandir}/man1/


%check
%pytest -v


%files -f %{pyproject_files}
%doc CHANGELOG.md README.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%doc %{_docdir}/%{name}/asciicast-v1.md
%doc %{_docdir}/%{name}/asciicast-v2.md
%{_bindir}/asciinema
%{_mandir}/man1/%{name}.1*


%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 15 2022 Carl George <carl@george.computer> - 2.2.0-4
- Use %%pyproject_files to simplify %%files
- Remove duplicate license file

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.2.0-3
- Rebuilt for Python 3.11

* Wed Jun 08 2022 Charalampos Stratakis <cstratak@redhat.com> - 2.2.0-2
- Utilize pytest instead of the deprecated nose test runner

* Sat May 07 2022 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 2.2.0-1
- Upgrade to latest upstream, change to pyproject build

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Oct 03 2021 Carl George <carl@george.computer> - 2.1.0-1
- Latest upstream
- Resolves: rhbz#2010110

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.2-7
- Rebuilt for Python 3.10

* Tue Feb 23 2021 Carl George <carl@george.computer> - 2.0.2-6
- Add patch to avoid tput (ncurses) requirement

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-3
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 10 2019 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 2.0.2-1
- Upgrade to version 2.0.2

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-8
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.1-5
- Add setuptools back to requires

* Mon Aug 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.1-4
- Fixup license tag
- Trivial cleanups in packaging

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-2
- Rebuilt for Python 3.7

* Mon Apr 16 2018 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 2.0.1-1
- Update to version 2.0.1

* Mon Feb 12 2018 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 2.0.0-1
- Update to version 2.0.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 12 2017 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 1.4.0-1
- Update to version 1.4.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Jul 17 2016 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 1.3.0-1
- update to version 1.3.0
- Rewritten from Go to python3

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-4
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun  3 2015 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 1.1.0-1
- Update to new version

* Mon Mar 23 2015 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 1.0.0-2
- Patch: support locale which ends with utf8
- Patch: edit some details in man page

* Tue Mar 17 2015 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 1.0.0-1
- Update to new version
- Add Godeps to docs

* Fri Mar  6 2015 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.9.9-1
- Update to new version
- Rewritten to Go
- License changed to GPLv3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 10 2014 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.9.8-1
- Update to new version

* Mon Jan 27 2014 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.9.7-3
- Add check of tests
- Add build and common requires
- Patch for non-interactive shell

* Mon Dec  2 2013 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.9.7-2
- A few spec file changes
- Edit Summary

* Mon Nov 25 2013 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.9.7-1
- Initial package
