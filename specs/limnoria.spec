%global upstreamver 2024-05-31

Name:           limnoria
Version:        20240531
Release:        2%{?dist}
Summary:        A modified version of Supybot (an IRC bot) with enhancements and bug fixes

License:        BSD-3-Clause AND GPL-2.0-only AND GPL-2.0-or-later
#
# The bulk of the package is BSD-3-Clause.
# Parts of the Math plugin are GPL-2.0-only
# The Dict plugin is GPL-2.0-or-later
#
URL:            https://github.com/ProgVal/Limnoria
Source0:        https://github.com/ProgVal/Limnoria/archive/master-%{upstreamver}.tar.gz

BuildArch:      noarch

# Provide the upper case version also to avoid confusion
Provides: Limnoria = %{version}-%{release}

#
# Obsolete the supybot-gribble package as this is a newer/maintained fork.
#
Obsoletes: supybot-gribble =< 0.83.4.1-18%{dist}
Provides: supybot-gribble = 0.83.4.1-19%{dist}

BuildRequires:  python3-devel
BuildRequires:  python3-chardet
BuildRequires:  python3-pytz
BuildRequires:  python3-dateutil
BuildRequires:  python3-gnupg
BuildRequires:  python3-feedparser
BuildRequires:  python3-sqlalchemy
BuildRequires:  python3-pysocks
BuildRequires:  python3-ecdsa
BuildRequires:  python3-setuptools
Requires:  python3-devel
Requires:  python3-chardet
Requires:  python3-pytz
Requires:  python3-dateutil
Requires:  python3-gnupg
Requires:  python3-feedparser
Requires:  python3-sqlalchemy
Requires:  python3-pysocks
Requires:  python3-ecdsa

%description
Supybot is a robust (it doesn't crash), user friendly 
(it's easy to configure) and programmer friendly 
(plugins are extremely easy to write) Python IRC bot.
It aims to be an adequate replacement for most existing IRC bots.
It includes a very flexible and powerful ACL system for controlling 
access to commands, as well as more than 50 builtin plugins 
providing around 400 actual commands.

Limnoria is a project which continues development of Supybot 
(you can call it a fork) by fixing bugs and adding features 
(see the list of added features for more details).

%prep
%autosetup -n Limnoria-master-%{upstreamver}

%build
# remove stray python bits from debug plugin
sed -i 1"s|#!/usr/bin/python||" plugins/Debug/plugin.py

# This should be set to the day of the release. 
# It's gets added as 'version' and is based on build time, not release time.
SOURCE_DATE_EPOCH=`date --date=%{version} +\%s`
export SOURCE_DATE_EPOCH

%{__python3} setup.py build

%install
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

# TODO: get tests working
#check

%files
%doc ChangeLog CONTRIBUTING.md README.md RELNOTES
%license LICENSE.md
%{_bindir}/supybot
%{_bindir}/supybot-adduser
%{_bindir}/supybot-botchk
%{_bindir}/supybot-plugin-create
%{_bindir}/supybot-plugin-doc
%{_bindir}/supybot-test
%{_bindir}/supybot-wizard
%{_bindir}/supybot-reset-password
%{_mandir}/man1/supybot-adduser.1.gz
%{_mandir}/man1/supybot-botchk.1.gz
%{_mandir}/man1/supybot-plugin-create.1.gz
%{_mandir}/man1/supybot-plugin-doc.1.gz
%{_mandir}/man1/supybot-test.1.gz
%{_mandir}/man1/supybot-wizard.1.gz
%{_mandir}/man1/supybot.1.gz
%{_mandir}/man1/supybot-reset-password.1.gz
%{_bindir}/limnoria
%{_bindir}/limnoria-adduser
%{_bindir}/limnoria-botchk
%{_bindir}/limnoria-plugin-create
%{_bindir}/limnoria-plugin-doc
%{_bindir}/limnoria-test
%{_bindir}/limnoria-wizard
%{_bindir}/limnoria-reset-password
%{_mandir}/man1/limnoria-adduser.1.gz
%{_mandir}/man1/limnoria-botchk.1.gz
%{_mandir}/man1/limnoria-plugin-create.1.gz
%{_mandir}/man1/limnoria-plugin-doc.1.gz
%{_mandir}/man1/limnoria-test.1.gz
%{_mandir}/man1/limnoria-wizard.1.gz
%{_mandir}/man1/limnoria.1.gz
%{_mandir}/man1/limnoria-reset-password.1.gz
%{python3_sitelib}/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20240531-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Kevin Fenzi <kevin@scrye.com> - 20240531-1
- Update to 20240531 and drop old no longer used python2 bits.

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20231209-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 20231209-4
- Rebuilt for Python 3.13

* Mon Mar 25 2024 Nils Philippsen <nils@tiptoe.de> - 20231209-3
- Revert constraining SQLAlchemy version

* Thu Mar 21 2024 Nils Philippsen <nils@tiptoe.de> - 20231209-2
- Require SQLAlchemy < 2

* Wed Feb 14 2024 Kevin Fenzi <kevin@scrye.com> - 20231209-1
- Update to 2023-12-09.

* Wed Feb 14 2024 Michel Lind <salimma@fedoraproject.org> - 20230211-6
- Remove unused python3-mock test dependency
- Use SPDX license identifiers

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20230211-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20230211-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20230211-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 20230211-2
- Rebuilt for Python 3.12

* Sun Feb 26 2023 Kevin Fenzi <kevin@scrye.com> - 20230211-1
- Update to 2023-02-11

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20220703-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jul 31 2022 Kevin Fenzi <kevin@scrye.com> - 20220703-7
- Update to 2022-07-03

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20210527-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 20210527-6
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20210527-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20210527-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 20210527-3
- Rebuilt for Python 3.10

* Sat May 29 2021 Kevin Fenzi <kevin@scrye.com> - 20210527-2
- Fix changelog

* Sat May 29 2021 Kevin Fenzi <kevin@scrye.com> - 20210527-1
- Upgrade to 20210527

* Fri May 28 2021 Simo Sorce <simo@fedoraproject.org> - 20210411-2
- Fix version string forever by calculating it

* Sat Apr 24 2021 Kevin Fenzi <kevin@scrye.com> - 20210411-1
- Upgrade to 20210411.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20201013-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 03 2020 Kevin Fenzi <kevin@scrye.com> - 20201013-1
- Update to 20201013.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20200701-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 12 2020 Kevin Fenzi <kevin@scrye.com> - 20200701-1
- Update to 20200701.

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 20200319-2
- Rebuilt for Python 3.9

* Sun Apr 05 2020 Kevin Fenzi <kevin@scrye.com> - 20200319-1
- Update to 20200319. 

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20191109-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 10 2019 Kevin Fenzi <kevin@scrye.com> - 20191109-2
- Fix incorrect version reporting.

* Sat Nov 09 2019 Kevin Fenzi <kevin@scrye.com> - 20191109-1
- Update to 2019-11-09

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 20180625.2-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 20180625.2-5
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20180625.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20180625.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 02 2018 Kevin Fenzi <kevin@scrye.com> - 20180625.2-2
- Switch to python3 by default in f29+

* Fri Jul 20 2018 Kevin Fenzi <kevin@scrye.com> - 20180625.2-1
- Update to 2018-06-25-2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20171025-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 Iryna Shcherbina <ishcherb@redhat.com> - 20171025-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20171025-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 01 2017 Kevin Fenzi <kevin@scrye.com> - 20171025-1
- Update to 20171025.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170127-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 07 2017 Kevin Fenzi <kevin@scrye.com> - 20170127-1
- Update to 20170127

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20160506-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jun 07 2016 Kevin Fenzi <kevin@scrye.com> - 20160506-2
- Updates from review: Fixed license
- Added Run time requires for needed python packages. 

* Sat Jun 04 2016 Kevin Fenzi <kevin@scrye.com> - 20160506-1
- Initial Fedora/EPEL version
