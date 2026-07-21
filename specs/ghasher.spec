Name:           ghasher
Version:        1.2.1
Release:        %autorelease
Summary:        GUI hasher for GTK+ 2
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://asgaard.homelinux.org/code/ghasher/
Source:         http://asgaard.homelinux.org/code/ghasher/ghasher-%{version}.tar.gz
ExcludeArch:    %{ix86}
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gtk2-devel >= 2.4
BuildRequires:  libglade2-devel
BuildRequires:  make
BuildRequires:  openssl-devel
Patch:          %{name}-format-security.patch
Patch:          %{name}-openssl-1.1.0.patch

%description
ghasher can easily show the MD5 sum (or md2, md4, sha1, sha, ripemd160, dss1)
of a file. Motivation for this utility was that users shouldn't need to open a
command line for checking the MD5 sum of files they download.

%prep
%autosetup

%build
%make_build CFLAGS="%{optflags} -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE $(pkg-config gtk+-2.0 libglade-2.0 --cflags)" LDFLAGS="%{build_ldflags} $(pkg-config gtk+-2.0 libglade-2.0 --libs) -lcrypto"

%install
install -p -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -p -D -m 0644 hash.xpm %{buildroot}%{_datadir}/pixmaps/hash.xpm

cat > %{name}.desktop << EOF
[Desktop Entry]
Name=MD5 Sum Utility
Comment=Calculate the md5 sum of a file
Exec=ghasher %%F
Terminal=false
Type=Application
Icon=hash
Categories=Utility;GTK;
EOF
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  %{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc AUTHORS NEWS README TODO
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/hash.xpm

%changelog
%autochangelog
