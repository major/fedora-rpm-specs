%global pugixml_version 1.15
%global short pwsafe

Summary:        Password Safe is a password management utility
Name:           passwordsafe
Version:        1.25.0
Source0:        https://github.com/%{short}/%{short}/archive/refs/tags/%{version}/%{short}-%{version}.tar.gz
Source1:        https://github.com/%{short}/%{short}/releases/download/%{version}/%{version}.tar.gz.sig
Source2:        ronys-at-pwsafe-dot-org.gpg
Release:        %autorelease
Url:            https://pwsafe.org/

# https://github.com/pwsafe/pwsafe/pull/1792
# upstream wants to keep this libmagic reference since it will be needed
# when pwsafe-cli can handle attachments
Patch2:         remove-unreferenced-libmagic.patch
# https://github.com/pwsafe/pwsafe/pull/1789
# upstream wants to keep utf8 bom since they seem to have Windows editors
# that require it. I don't think any Fedora editor requires a utf-8 bom.
Patch3:         bomless-utf8-output.patch
#
# S390 C++ does not allow variable length arrays
Patch4:         https://github.com/pwsafe/pwsafe/pull/1875.patch

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
# for source file verification
BuildRequires:  gpgverify
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
Recommends:     %{name}-doc
Suggests:       xvkbd

# this package cannot directly use the fedora pugixml library, since
# that is built for char, and we need the wchar version.
Provides:       bundled(pugixml) = %{pugixml_version}

%global doc_files %{shrink:
    README.md
    README.LINUX.md
    docs/ChangeLog.md
    docs/ReleaseNotes.md
    docs/ReleaseNotesWX.md
    docs/config.txt
    docs/formatV1.txt
    docs/formatV2.txt
    docs/formatV3.txt
    docs/formatV4.txt
    docs/help.txt
    docs/pwsafe-state-machine.rtf
}

%description
Password Safe is a password manager.  It stores your passwords in an
encrypted file, allowing you to remember only one password (the
"master password"), instead of all the username/password combinations
that you use.  For extra security, you can use a Yubikey device to
provide two-factor authentication.

Password Safe runs on Windows, Linux, macOS and FreeBSD.


%package doc
Summary:   Password Safe help files
BuildArch: noarch
License:   Artistic-2.0

%description doc
The passwordsafe-doc package contains the help files for Password Safe.
They are ZIP archives whose contents can be accessed directly (without
extraction) from the Password Safe GUI (Help menu or button).


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%autosetup -p1 -n %{short}-%{version}
# make sure our binaries don't depend on any windows/mac stuff
rm -r src/ui/Windows
rm -r src/os/windows
rm -r src/os/mac


%conf
%cmake -DGTEST_BUILD=OFF


%build
%cmake_build
#
cp -a src/core/crypto/external/Chromium/LICENSE Chromium.LICENSE
#
# actually in .md format
mv docs/ChangeLog.txt docs/ChangeLog.md
# fedora automated review complains about line endings
dos2unix --info %{doc_files} | cat -n
dos2unix --info=c %{doc_files} | xargs dos2unix --verbose --keepdate


%install
%cmake_install
%find_lang pwsafe


%check
%ctest
desktop-file-validate %{buildroot}/%{_datadir}/applications/pwsafe.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.pwsafe.pwsafe.metainfo.xml


%files -f pwsafe.lang
%license LICENSE
%license Chromium.LICENSE
%license pugixml.LICENSE
%doc %{doc_files}
%{_bindir}/pwsafe
%{_bindir}/pwsafe-cli
%{_mandir}/man1/pwsafe.1*
%{_datadir}/applications/pwsafe.desktop
%{_datadir}/icons/*/*/*/pwsafe.png
%{_metainfodir}/org.pwsafe.pwsafe.metainfo.xml
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/xml

%files doc
%license LICENSE
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/help


%changelog
%autochangelog
