Name:           python-nbxmpp
Version:        4.5.4
Release:        2%{?dist}
Summary:        Python library for non-blocking use of Jabber/XMPP
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://dev.gajim.org/gajim/python-nbxmpp/
Source0:        https://dev.gajim.org/gajim/python-nbxmpp/-/archive/%{version}/python-nbxmpp-%{version}.tar.bz2

BuildArch:      noarch
BuildRequires:  python3-devel

%global desc %{expand:
python-nbxmpp is a Python library that provides a way for Python applications
to use Jabber/XMPP networks in a non-blocking way.}

%description
%{desc}

%package -n python3-nbxmpp
Summary:        %{summary}
Requires:       python3-gobject >= 3.42.0
Requires:       glib2 >= 2.66
Requires:       libsoup3
Recommends:     python3-gssapi
Obsoletes:      python-nbxmpp-doc < 1.0.0

%description -n python3-nbxmpp
%{desc}

%prep
%autosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files nbxmpp

%files -n python3-nbxmpp -f %{pyproject_files}
%doc README.md ChangeLog

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 13 2024 Michael Kuhn <suraia@fedoraproject.org> - 4.5.4-1
- Update to 4.5.4

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 4.3.1-7
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 4.3.1-2
- Rebuilt for Python 3.12

* Sun Jun 04 2023 Michael Kuhn <suraia@fedoraproject.org> - 4.3.1-1
- Update to 4.3.1

* Sat May 27 2023 Michael Kuhn <suraia@fedoraproject.org> - 4.3.0-1
- Update to 4.3.0

* Sun Mar 26 2023 Michael Kuhn <suraia@fedoraproject.org> - 4.2.2-1
- Update to 4.2.2

* Sun Mar 19 2023 Michael Kuhn <suraia@fedoraproject.org> - 4.2.1-1
- Update to 4.2.1

* Thu Feb 09 2023 Michael Kuhn <suraia@fedoraproject.org> - 4.2.0-1
- Update to 4.2.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jan 14 2023 Michael Kuhn <suraia@fedoraproject.org> - 4.0.1-1
- Update to 4.0.1

* Sat Jan 07 2023 Michael Kuhn <suraia@fedoraproject.org> - 4.0.0-1
- Update to 4.0.0

* Mon Oct 31 2022 Michael Kuhn <suraia@fedoraproject.org> - 3.2.5-1
- Update to 3.2.5

* Sun Oct 09 2022 Michael Kuhn <suraia@fedoraproject.org> - 3.2.4-1
- Update to 3.2.4

* Mon Sep 19 2022 Michael Kuhn <suraia@fedoraproject.org> - 3.2.2-1
- Update to 3.2.2

* Wed Jul 27 2022 Michael Kuhn <suraia@fedoraproject.org> - 3.1.1-1
- Update to 3.1.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 27 2022 Michael Kuhn <suraia@fedoraproject.org> - 3.1.0-3
- Rebuild for Python 3.11

* Thu Jun 02 2022 Michael Kuhn <suraia@fedoraproject.org> - 3.1.0-2
- Fix GLib dependency

* Thu Jun 02 2022 Michael Kuhn <suraia@fedoraproject.org> - 3.1.0-1
- Update to 3.1.0
- Update to newer Python packaging guidelines

* Sat May 21 2022 Michael Kuhn <suraia@fedoraproject.org> - 3.0.2-1
- Update to 3.0.2

* Sat May 14 2022 Michael Kuhn <suraia@fedoraproject.org> - 3.0.1-1
- Update to 3.0.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Oct 09 2021 Michael Kuhn <suraia@fedoraproject.org> - 2.0.4-1
- Update to 2.0.4

* Sat Aug 07 2021 Michael Kuhn <suraia@fedoraproject.org> - 2.0.3-1
- Update to 2.0.3

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.2-2
- Rebuilt for Python 3.10

* Sun Feb 21 2021 Michael Kuhn <suraia@fedoraproject.org> - 2.0.2-1
- Update to 2.0.2

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Michal Schmidt <mschmidt@redhat.com> - 1.0.0-1
- Upstream release 1.0.0.

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.10-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.10-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.10-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 25 2019 Michal Schmidt <mschmidt@redhat.com> - 0.6.10-1
- Upstream release 0.6.10.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Michal Schmidt <mschmidt@redhat.com> - 0.6.9-1
- Upstream release 0.6.9.

* Wed Nov 14 2018 Michal Schmidt <mschmidt@redhat.com> - 0.6.8-1
- Upstream release 0.6.8.

* Thu Oct 11 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6.6-4
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6.6-2
- Rebuilt for Python 3.7

* Mon May 21 2018 Michal Schmidt <mschmidt@redhat.com> - 0.6.6-1
- Upstream release 0.6.6.

* Mon Mar 19 2018 Michal Schmidt <mschmidt@redhat.com> - 0.6.4-1
- Upstream release 0.6.4.

* Wed Mar 07 2018 Michal Schmidt <mschmidt@redhat.com> - 0.6.3-1
- Upstream release 0.6.3.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Michal Schmidt <mschmidt@redhat.com> - 0.6.2-1
- Upstream release 0.6.2.

* Mon Dec 04 2017 Michal Schmidt <mschmidt@redhat.com> - 0.6.1-1
- Upstream release 0.6.1.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 08 2017 Michal Schmidt <mschmidt@redhat.com> - 0.5.6-1
- Upstream release 0.5.6.

* Mon Feb 06 2017 Michal Schmidt <mschmidt@redhat.com> - 0.5.5-1
- Upstream release 0.5.5.
- New upstream location and tarball format.
- Refer to python2-kerberos using its actual package name.

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.5.3-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 18 2016 Michal Schmidt <mschmidt@redhat.com> - 0.5.3-3
- Build as both python2-nbxmpp and python3-nbxmpp. (#1309621)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 27 2015 Matej Cepl <mcepl@redhat.com> - 0.5.3-1
- Upstream release 0.5.3.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 02 2015 Michal Schmidt <mschmidt@redhat.com> - 0.5.2-1
- Upstream bugfix release 0.5.2.

* Thu Oct 16 2014 Michal Schmidt <mschmidt@redhat.com> - 0.5.1-1
- New upstream release, required by Gajim 0.16.

* Mon Aug 11 2014 Michal Schmidt <mschmidt@redhat.com> - 0.5-1
- New upstream release.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 19 2014 Michal Schmidt <mschmidt@redhat.com> - 0.4-1
- Initial Fedora packaging.
