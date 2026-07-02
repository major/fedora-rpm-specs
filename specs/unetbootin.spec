Name:           unetbootin
Version:        702
Release:        %autorelease
Summary:        Create bootable Live USB drives for a variety of Linux distributions
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://unetbootin.github.io/
Source0:        https://sourceforge.net/projects/%{name}/files/UNetbootin/%{version}/%{name}-source-%{version}.tar.gz
Patch0:         unetbootin-675-desktop.patch
# Syslinux is only available on x86 architectures
ExclusiveArch:  %{ix86} x86_64 aarch64

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
# Not picked up automatically, required for operation
Requires:       p7zip-plugins
%ifarch %{ix86} x86_64
Requires:       syslinux
Requires:       syslinux-extlinux
%endif

%description
UNetbootin allows you to create bootable Live USB drives for a variety of
Linux distributions from Windows or Linux, without requiring you to burn a CD.
You can either let it download one of the many distributions supported
out-of-the-box for you, or supply your own Linux .ISO file if you've already
downloaded one or your preferred distribution isn't on the list.


%prep
%autosetup -c
# Fix line endings
sed -i 's/\r$//' README.TXT
# Fix desktop file
sed -i '/^RESOURCES/d' unetbootin.pro

%build
lupdate-qt5 unetbootin.pro
lrelease-qt5 unetbootin.pro
%qmake_qt5
%make_build


%install
install -D -p -m 755 unetbootin %{buildroot}%{_bindir}/unetbootin
# Install desktop file
desktop-file-install --dir=%{buildroot}%{_datadir}/applications unetbootin.desktop
# Install localization files
install -d %{buildroot}%{_datadir}/unetbootin
install -c -p -m 644 unetbootin_*.qm %{buildroot}%{_datadir}/unetbootin/
# Install pixmap
install -D -p -m 644 unetbootin_512.png %{buildroot}%{_datadir}/pixmaps/unetbootin.png

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/unetbootin.desktop

%files
%doc README.TXT
%{_bindir}/unetbootin
%{_datadir}/unetbootin/
%{_datadir}/applications/unetbootin.desktop
%{_datadir}/pixmaps/unetbootin.png

%changelog
%autochangelog
