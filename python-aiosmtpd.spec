%global pkgname aiosmtpd
%global summary Asyncio-based SMTP server
%global _description \
This is a server for SMTP and related protocols, similar in utility \
to the standard library’s smtpd.py module, but rewritten to be based \
on asyncio for Python 3.
%global srcname %{pkgname}
%global with_docs 0


Name:           python-%{pkgname}
Version:        1.4.4.post2
Release:        2%{?dist}
Summary:        %{summary}

License:        ASL 2.0
URL:            https://github.com/aio-libs/aiosmtpd
Source0:        %{url}/archive/%{version}/%{pkgname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel >= 3.4
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-atpublic
BuildRequires:  python%{python3_pkgversion}-flufl-testing
BuildRequires:  python%{python3_pkgversion}-attrs
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-pytest-mock
# Required for tests
BuildRequires:  git-core
%if 0%{?with_docs}
BuildRequires:  python%{python3_pkgversion}-sphinx
%endif

%description %{_description}


%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        %{summary}
Requires:       python%{python3_pkgversion}-atpublic
Requires:       python%{python3_pkgversion}-attrs
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkgname}}

%description -n python%{python3_pkgversion}-%{pkgname} %{_description}


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install
# Cleanups
rm -rf %{buildroot}%{python3_sitelib}/examples
rm -f  %{buildroot}%{python3_sitelib}/aiosmtpd/docs/.gitignore


%check
%{__python3} -m pytest -v


%files -n python%{python3_pkgversion}-%{pkgname}
%doc README.rst examples
%if 0%{?with_docs}
%doc build/sphinx/html
%endif
%{_bindir}/aiosmtpd
%{python3_sitelib}/aiosmtpd/
%{python3_sitelib}/aiosmtpd-*.egg-info/


%changelog
* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 1.4.4.post2-2
- Rebuilt for Python 3.12

* Sat May 13 2023 Neal Gompa <ngompa@fedoraproject.org> - 1.4.4.post2-1
- Update to 1.4.4.post2

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.4.2-8
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Sep 23 2021 Miro Hrončok <mhroncok@redhat.com> - 1.4.2-6
- Avoid SSLError: Cannot create a client socket with a PROTOCOL_TLS_SERVER context

* Fri Sep 17 2021 Neal Gompa <ngompa@fedoraproject.org> - 1.4.2-5
- Backport patches for some Python 3.10 support

* Fri Sep 17 2021 Neal Gompa <ngompa@fedoraproject.org> - 1.4.2-4
- Allow tests to fail to fix FTBFS

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.4.2-2
- Rebuilt for Python 3.10

* Tue Mar 30 2021 Neal Gompa <ngompa13@gmail.com> - 1.4.2-1
- Rebase to 1.4.2
- Drop unused alternate build logic

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 30 2019 Aurelien Bompard <abompard@fedoraproject.org> - 1.2.1-2
- Fix build

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 20 2018 Aurelien Bompard <abompard@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 03 2017 Aurelien Bompard <abompard@fedoraproject.org> - 1.0-0.1.a5
- Update to 1.0 final.

* Mon Apr 10 2017 Aurelien Bompard <abompard@fedoraproject.org> - 1.0-0.1.a5
- Update to 1.0a5.

* Wed Dec 14 2016 Aurelien Bompard <abompard@fedoraproject.org> - 1.0-0.1.a4
- Initial package.
