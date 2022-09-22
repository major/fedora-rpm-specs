%if 0%{?fedora}
  %bcond_without   pyproject
  %bcond_with      python2
  %bcond_with      python3
%else
  %bcond_with      pyproject
  %if 0%{?rhel} > 7
    %bcond_with    python2
    %bcond_without python3
  %else
    %bcond_without python2
    %bcond_with    python3
  %endif
%endif

%bcond_without check


%global sum()   Build manual page from %* ArgumentParser object
%global desc \
Generate manual page an automatic way from ArgumentParser object, so the \
manpage 1:1 corresponds to the automatically generated --help output.  The \
manpage generator needs to known the location of the object, user can \
specify that by (a) the module name or corresponding python filename and \
(b) the object name or the function name which returns the object. \
There is a limited support for (deprecated) optparse objects, too.


Name:           argparse-manpage
Version:        3
Release:        4%{?dist}
Summary:        %{sum Python}
BuildArch:      noarch

License:        ASL 2.0
URL:            https://github.com/praiskup/%{name}
Source0:        https://github.com/praiskup/%name/releases/download/v%version/%name-%version.tar.gz

# Fix tests compatibility with pip >= 21.3
# Fixed upstream: https://github.com/praiskup/argparse-manpage/pull/60
Patch1:         fix-pip-21.3-compat.patch

%if %{with python2}
BuildRequires: python2-setuptools python2-devel
%if %{with check}
%if 0%{?rhel} && 0%{?rhel} == 7
BuildRequires: pytest
%else
BuildRequires: python2-pytest
%endif
%endif
%endif

%if %{with python3}
BuildRequires: python3-setuptools python3-devel
%if %{with check}
BuildRequires: python3-pytest
%endif
%endif

%if %{with pyproject}
BuildRequires: python3-devel
%if %{with check}
BuildRequires: python3-pytest
%endif
%endif

%if %{with python3} || %{with pyproject}
Requires: python3-%name = %version-%release
%else
Requires: python2-%name = %version-%release
%endif

%description
%desc


%package -n     python2-%name
Summary:        %{sum Python 2}

%description -n python2-%name
%{desc}


%package -n     python3-%name
Summary:        %{sum Python 3}

%description -n python3-%name
%{desc}


%prep
%setup -q
%patch1 -p1

%if %{with pyproject}
%generate_buildrequires
%pyproject_buildrequires
%endif


%build
%if %{with python2}
%py2_build
%endif
%if %{with python3}
%py3_build
%endif
%if %{with pyproject}
%pyproject_wheel
%endif


%install
%if %{with python2}
%py2_install
%endif
%if %{with python3}
%py3_install
%endif
%if %{with pyproject}
%pyproject_install
%endif



%if %{with check}
%check
%if %{with python2}
PYTHONPATH=%buildroot%python2_sitearch %__python2 -m pytest -vv
%endif
%if %{with python3}
PYTHONPATH=%buildroot%python3_sitearch %__python3 -m pytest -vv
%endif
%if %{with pyproject}
%pytest
%endif
%endif


%files
%license LICENSE
%{_bindir}/argparse-manpage
%_mandir/man1/argparse-manpage.1.*
%if %{with python3} || %{with pyproject}
%python3_sitelib/build_manpages/cli.py
%else
%python2_sitelib/build_manpages/cli.py
%endif


%if %{with python2}
%files -n python2-%name
%license LICENSE
%python2_sitelib/build_manpages
%python2_sitelib/argparse_manpage-%{version}*.egg-info
%exclude %python2_sitelib/build_manpages/cli.py
%endif


%if %{with python3} || %{with pyproject}
%files -n python3-%name
%license LICENSE
%python3_sitelib/build_manpages
%if %{with pyproject}
%python3_sitelib/argparse_manpage-*dist-info
%else
%python3_sitelib/argparse_manpage-%{version}*.egg-info
%endif
%exclude %python3_sitelib/build_manpages/cli.py
%endif


%changelog
* Fri Jul 22 2022 Charalampos Stratakis <cstratak@redhat.com> - 3-4
- Fix tests compatibility with pip >= 21.3

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3-2
- Rebuilt for Python 3.11

* Wed Apr 27 2022 Pavel Raiskup <praiskup@redhat.com> - 3-1
- new upstream release: https://github.com/praiskup/argparse-manpage/releases/tag/v3

* Thu Mar 03 2022 Pavel Raiskup <praiskup@redhat.com> - 2.2-1
- new release - fix build for the setuptools v60+

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 12 2022 Pavel Raiskup <praiskup@redhat.com> - 2.1-1
- new upstream release:
  https://github.com/praiskup/argparse-manpage/releases/tag/v2.1

* Sun Nov 28 2021 Pavel Raiskup <praiskup@redhat.com> - 2-1
- new upstream release:
  https://github.com/praiskup/argparse-manpage/releases/tag/v2

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.5-3
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 14 2020 Pavel Raiskup <praiskup@redhat.com> - 1.5-1
- new release

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4-3
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 24 2020 Pavel Raiskup <praiskup@redhat.com> - 1.4-1
- new release to fix testsuite against Python 3.9

* Tue Jan 07 2020 Pavel Raiskup <praiskup@redhat.com> - 1.3-1
- new release

* Sat Sep 07 2019 Pavel Raiskup <praiskup@redhat.com> - 1.2.2-1
- new release

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1-6
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 02 2018 Pavel Raiskup <praiskup@redhat.com> - 1.1-3
- drop python3 on F30+ (rhbz#1634992)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 25 2018 Pavel Raiskup <praiskup@redhat.com> - 1.1-1
- v1.1

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-2
- Rebuilt for Python 3.7

* Mon Feb 19 2018 Pavel Raiskup <praiskup@redhat.com> - 1.0.0-1
- initial RPM packaging
