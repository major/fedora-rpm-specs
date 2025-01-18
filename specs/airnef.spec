%if 0%{?rhel} && 0%{?rhel} <= 7
%global python    python2
%global appdir    %python2_sitelib/%name
%global appresdir %python2_sitelib/%name/appresource
%else
%global python    python3
%global appdir    %python3_sitelib/%name
%global appresdir %python3_sitelib/%name/appresource
%endif


Name:           airnef
Version:        1.1
Release:        30%{?dist}
Summary:        Wireless download from your Nikon/Canon Camera

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            http://www.testcams.com/airnef/
BuildArch:      noarch
Source0:        http://www.testcams.com/airnef/Version_%{version}/airnef_v%{version}_Source.zip

Patch0:         airnef-1.1-rpm-paths.patch
Patch1:         airnef-1.1-missing-re-import.patch

BuildRequires:  %python-devel

Requires:       %python-six
Requires:       %python-tkinter

%description
Open-source utility for downloading images and videos from WiFi-equipped
cameras.  Airnef supports all Nikon cameras that have built-in WiFi interfaces,
along with those using external Nikon WU-1a and WU-1b WiFi adapters, Canon and
Sony cameras.


%prep
%autosetup -p1 -n airnef

# six is available in fedora
rm six.py

# OSX only file is not needed
rm airnefcmd_OSX_Frozen_Wrapper.py

# TODO: ??
rm appresource/airnef.icns

for i in `grep -l -r '#!/usr/bin/env python'`; do
    sed -i '1 s|#!/usr/bin/env python.*||g' "$i"
done


%build


%install
mkdir -p %buildroot%appdir
for i in *.py *.pyw; do
    dest=${i/%pyw/py} # drop pyw suffixes
    install "$i" -p -m 644 %buildroot%appdir/"$dest"
done

mkdir -p %buildroot%appresdir
for i in appresource/*; do
    install "$i" -p -m 644 %buildroot%appresdir
done

cat > wrapper <<'EOF'
#! /bin/sh
exec %python %appdir/"$(basename "$0").py" "$@"
EOF

mkdir -p %buildroot%_bindir
install -m 755 wrapper %buildroot%_bindir/airnef
install -m 755 wrapper %buildroot%_bindir/airnefcmd


%files
%doc
%_bindir/*
%dir %appdir
%appdir/*.py
%if "%python" == "python3"
%appdir/__pycache__
%else
%appdir/*.pyo
%appdir/*.pyc
%endif
%dir %appresdir
%appresdir/*.ico
%appresdir/*.gif
%appresdir/*.xbm


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1-29
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.1-27
- Rebuilt for Python 3.13

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.1-23
- Rebuilt for Python 3.12

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.1-20
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 04 2021 Pavel Raiskup <praiskup@redhat.com> - 1.1-18
- add missing 're' import, rhbz#1990073

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1-15
- Rebuilt for Python 3.10

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1-12
- Rebuilt for Python 3.9

* Thu Apr 02 2020 Björn Esser <besser82@fedoraproject.org> - 1.1-11
- Fix string quoting for rpm >= 4.16

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1-8
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 25 2019 Pavel Raiskup <praiskup@redhat.com> - 1.1-6
- require python3-tkinter (rhbz#1702714)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1-3
- Rebuilt for Python 3.7

* Wed May 30 2018 Pavel Raiskup <praiskup@redhat.com> - 1.1-2
- silent rpmdiff complaints about python shebangs (review rhbz#1583475)

* Tue May 29 2018 Pavel Raiskup <praiskup@redhat.com> - 1.1-1
- initial RPM packaging
