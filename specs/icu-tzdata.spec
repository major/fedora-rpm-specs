# remirepo spec file for icu-tzdata
#
# SPDX-FileCopyrightText:  Copyright 2026 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

Name:      icu-tzdata
Version:   2026f
License:   Unicode-DFS-2016
Release:   1%{?dist}
Summary:   Updated tzdata for libicu
URL:       https://github.com/unicode-org/icu-data

# don't want to download the full git repository
# run ./makesrc.sh to retrieve needed files
Source0:   %{name}-%{version}.tgz
Source1:   makesrc.sh

BuildArch:     noarch
# For check
BuildRequires: libicu-devel
BuildRequires: python3

# for /usr/share/icu ownership
Requires:      libicu


%description
%{summary}.


%prep
%setup -n icu-data


%install
install -p -m755 -d %{buildroot}%{_datadir}/icu
cp -pr tzdata/icunew/%{version}/44  %{buildroot}%{_datadir}/icu/tzdata


%check
: Check reported version
DIR=$(python3 -c 'import sys;print ("be" if sys.byteorder=="big" else "le")')
ICU_TIMEZONE_FILES_DIR=%{buildroot}%{_datadir}/icu/tzdata/$DIR %{_bindir}/icuinfo 2>&1 | grep tz.version | tee log
grep -q '>%{version}<' log


%files
%license LICENSE
%{_datadir}/icu/tzdata


%changelog
* Fri Oct 30 2026 Remi Collet <remi@remirepo.net> - 2026f-1
- new package

