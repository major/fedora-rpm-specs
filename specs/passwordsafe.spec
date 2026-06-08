%global pugixml_version 1.15

%global         forgeurl0 https://github.com/pwsafe/pwsafe
%global         version0  1.24.0
# Using a more recent snapshot of `master` to pull in various
# necessary patches until 1.25 is out
%global         date      20260604
%global         commit    1d41f7b
%forgemeta

Summary:        Password Safe is a password management utility
Name:           passwordsafe
Version:        %forgeversion
Source0:        %forgesource0
Release:        %autorelease

# https://github.com/pwsafe/pwsafe/pull/1792
# upstream wants to keep this libmagic reference since it will be needed
# when pwsafe-cli can handle attachments
Patch2:         remove-unreferenced-libmagic.patch
# https://github.com/pwsafe/pwsafe/pull/1789
# upstream wants to keep utf8 bom since they seem to have Windows editors
# that require it. I don't think any Fedora editor requires a utf-8 bom.
Patch3:         bomless-utf8-output.patch
# update bundled pugixml to 1.15
Patch4:         https://github.com/pwsafe/pwsafe/pull/1807.patch
Url:            https://pwsafe.org/
#
# most of the code is Artistic-2.0
# src/core/crypto/external/Chromium is BSD-3-Clause
# src/core/pugixml is MIT
#
License:        Artistic-2.0 AND BSD-3-Clause AND MIT
# basic requirements to build the package
BuildRequires:  cmake gcc-c++ perl-interpreter
# for % check section
BuildRequires:  desktop-file-utils libappstream-glib
# for line ending fixups
BuildRequires:  dos2unix
# system libraries used by this package
BuildRequires:  file-devel
BuildRequires:  gtest-devel
BuildRequires:  libXt-devel
BuildRequires:  libXtst-devel
BuildRequires:  libcurl-devel
BuildRequires:  libuuid-devel
BuildRequires:  libyubikey-devel
BuildRequires:  openssl-devel
BuildRequires:  qrencode-devel
BuildRequires:  wxBase-devel
BuildRequires:  wxGTK-devel
BuildRequires:  xerces-c-devel
BuildRequires:  ykpers-devel
# since we have icons
Requires:       hicolor-icon-theme
Obsoletes:      pwsafe < 2.0.0-1

# this package cannot directly use the fedora pugixml library, since
# that is built for char, and we need the wchar version.
Provides:       bundled(pugixml) = %{pugixml_version}


%description

Password Safe is a password manager.  It stores your passwords in an
encrypted file, allowing you to remember only one password (the
"master password"), instead of all the username/password combinations
that you use.  For extra security, you can use a Yubikey device to
provide two-factor authentication.

Password Safe runs on Windows, Linux, macOS and FreeBSD.


%package doc
Summary:   Documentation and help files for Password Safe
BuildArch: noarch
License:   Artistic-2.0
Requires:  %{name} = %version-%release
%description doc
The passwordsafe-doc package contains the documentation
and help files for Password Safe.

%prep
%forgeautosetup -p1
# make sure our binaries don't depend on any windows/mac stuff
rm -rv src/ui/Windows
rm -rv src/os/windows
rm -rv src/os/mac
# kill off executable bit on all files
chmod -R -x+X .


%conf
%cmake -DGTEST_BUILD=OFF


%build
%cmake_build
#
cp -a src/core/crypto/external/Chromium/LICENSE Chromium.LICENSE
#
cd docs
# fedora automated review complains about line endings
dos2unix -k config.txt
dos2unix -k help.txt
# actually in .md format
mv ChangeLog.txt ChangeLog.md


%install
%cmake_install
%find_lang pwsafe
install -m 644 -D README.md      %{buildroot}%{_datadir}/doc/%{name}-%{version}/README.md
for x in ChangeLog.md \
         config.txt \
         formatV1.txt \
         formatV2.txt \
         formatV3.txt \
         formatV4.txt \
         help.txt \
         pwsafe-state-machine.rtf \
         ReleaseNotes.md \
         ReleaseNotesWX.md; do
    install -m 644 docs/$x  %{buildroot}%{_datadir}/doc/%{name}-%{version}/$x
done


%check
%ctest
desktop-file-validate %{buildroot}/%{_datadir}/applications/pwsafe.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.pwsafe.pwsafe.metainfo.xml



%files -f pwsafe.lang
%{_bindir}/pwsafe
%{_bindir}/pwsafe-cli
%license LICENSE
%license Chromium.LICENSE
%license pugixml.LICENSE
%{_mandir}/man1/pwsafe.1.gz
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/xml
%{_datadir}/applications/pwsafe.desktop
%{_datadir}/icons/*/*/*/pwsafe.png
%{_metainfodir}/org.pwsafe.pwsafe.metainfo.xml

%files doc
%docdir %{_datadir}/doc/%{name}-%{version}
%license LICENSE
%{_datadir}/doc/%{name}-%{version}
%{_datadir}/%{name}/help


%changelog
%autochangelog
