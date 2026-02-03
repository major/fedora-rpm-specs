Name:           rauc
Version:        1.15.1
Release:        %autorelease -b 1
Summary:        Safe and secure software updates for embedded Linux

License:        LGPL-2.1-or-later AND CC0-1.0
URL:            https://rauc.io/
Source0:        https://github.com/rauc/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz

# Debian: grub_editenv
# Fedora: grub2_editenv
# Upstream: Work has not yet begun
Patch0:         rauc_patch0_grub_editenv_debian_compat_fix.patch

# 1 test does not work due to network access
# Upstream: Work has not yet begun
Patch1:         rauc_patch1_disable_http_test.patch

# Exclude architectures that does not have grub2-tools-minimal package
ExcludeArch:    s390 s390x i686

# Tool requirements
BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  dbus-devel
BuildRequires:  glib2-devel
BuildRequires:  json-glib-devel
BuildRequires:  libcurl-devel
BuildRequires:  libfdisk-devel
BuildRequires:  libnl3-devel
BuildRequires:  openssl-devel
BuildRequires:  systemd-devel

# Make sure /usr/share/dbus-1/interfaces and /usr/share/dbus-1 are owned.
Requires:       dbus-common
# Weak dependency on documentation
Recommends:     rauc-doc

# Test requirements
BuildRequires:  dbus-daemon
BuildRequires:  e2fsprogs
BuildRequires:  fakeroot
BuildRequires:  grub2-tools-minimal
BuildRequires:  openssl
BuildRequires:  python3-dasbus
BuildRequires:  python3-pyasn1
BuildRequires:  python3-pyasn1-modules
BuildRequires:  python3-pytest
BuildRequires:  python3-requests
BuildRequires:  squashfs-tools

%package doc
Summary:        RAUC documentation

# rauc-doc does not contain any binaries
BuildArch:      noarch

# Documentation requirements
BuildRequires:  make
BuildRequires:  texinfo
BuildRequires:  thorvg
BuildRequires:  python3dist(docutils)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-sphinx_rtd_theme

%description doc
Documentation for RAUC.

%description
RAUC is a lightweight update client that runs on your Embedded Linux device
and reliably controls the procedure of updating your device with a new firmware
revision. RAUC is also the tool on your host system that lets you create,
inspect and modify update artifacts for your device.
Service is not installed as that is only needed on device.

%prep
%autosetup -v -N
# Debian vs. Fedora grub2 packaging difference
%patch -P 0 -b .orig
# rauc:pytest-http fails with Connection refused on 127.0.0.1
%patch -P 1 -b .orig
# Debian vs. Fedora grub2 packaging difference
cd test/bin
ln -sf grub-editenv grub2-editenv

%build
%meson \
        -Dfuzzing=false \
        -Dhtmldocs=false \
        -Dmanpages=true \
        -Dservice=false \
        -Dstreaming=false \
        -Dnetwork=false \
        -Dpkcs11_engine=false

%meson_build

# docbook for yelp or khelpcenter
pushd docs
# Yelp SVG image workaround
# https://gitlab.gnome.org/GNOME/yelp/-/issues/92
pushd images
# >=F43: tvg-svg2png
# <=F42: tvg_svg2png
tvg-svg2png . || tvg_svg2png .
popd
sed -i "s/\.svg/\.png/g" *.rst
tvg-svg2png RAUC_Logo_outline.svg || tvg_svg2png RAUC_Logo_outline.svg
sed -i "s/html_logo = 'RAUC_Logo_outline.svg'/html_logo = 'RAUC_Logo_outline.png'/g" conf.py
sphinx-build . texinfo -b texinfo
pushd texinfo
makeinfo --docbook %{name}.texi
popd
popd

%install
%meson_install

# docbook for yelp or khelpcenter
mkdir -p %{buildroot}%{_datadir}/help/en/%{name}
install -m644 docs/texinfo/%{name}.xml %{buildroot}%{_datadir}/help/en/%{name}
cp -p -r docs/texinfo/%{name}-figures %{buildroot}%{_datadir}/help/en/%{name}

%check
%meson_test

%files
%{_bindir}/rauc
%{_datadir}/dbus-1/interfaces/de.pengutronix.rauc.Installer.xml
%license COPYING LICENSES/CC0-1.0.txt
%doc README.rst CHANGES
%{_mandir}/man1/rauc.1.*

# docbook for yelp or khelpcenter
%files doc
%license COPYING
%dir %{_datadir}/help/en
%doc %lang(en) %{_datadir}/help/en/%{name}

%changelog
* Sun Feb 1 2026 Bruno Thomsen <bruno.thomsen@gmail.com> - 1.15.1-1
- Update package from 1.14 to 1.15.1
- Remove upstreamed patches
- Rework disabled tests patch

* Mon Jul 21 2025 Bruno Thomsen <bruno.thomsen@gmail.com> - 1.14-12
- Update patch 4 with CC0-1.0.txt and include it in rauc license
- Add COPYING to rauc-doc license
- Fix license as LGPL-2.1-or-later not LGPL-2.1-only

* Sat Jul 12 2025 Bruno Thomsen <bruno.thomsen@gmail.com> - 1.14-11
- Don't mark man page as doc
- Update patches against upstream version
- Yelp SVG image workaround: Convert SVG to PNG using thorvg
- thorvg workaround due to command rename in F42/F43

* Fri Jun 13 2025 Bruno Thomsen <bruno.thomsen@gmail.com> - 1.14-10
- Mark man page as doc
- Use same indentation on statements

* Tue Jun 10 2025 Bruno Thomsen <bruno.thomsen@gmail.com> - 1.14-9
- Recommend installing separate doc package

* Tue Jun 10 2025 Bruno Thomsen <bruno.thomsen@gmail.com> - 1.14-8
- Split large documentation into separate doc package

* Wed May 28 2025 Bruno Thomsen <bruno.thomsen@gmail.com> - 1.14-7
- Change dbus-common dependency from BuildRequires to Requires
- Update upstream license issue and update license information
- Generate docbook for yelp or khelpcenter

* Tue May 20 2025 Bruno Thomsen <bruno.thomsen@gmail.com> - 1.14-6
- Exclude some architectures that does not have grub2-tools-minimal package
- Add upstream xml file license issue link

* Mon May 19 2025 Bruno Thomsen <bruno.thomsen@gmail.com> - 1.14-5
- Add dbus-common dependency as xml is installed in dbus-1 directory
- Cleanup patches into 3 logical changes and update upstream status
- Add upstream status of RPM lint incorrect-fsf-address error

* Sat Apr 12 2025 Bruno Thomsen <bruno.thomsen@gmail.com> - 1.14-4
- Disable 5 tests that does not work on F43/rawhide
- Update files section with macros and add patch comments

* Wed Apr 9 2025 Bruno Thomsen <bruno.thomsen@gmail.com> - 1.14-3
- Disable network and streaming
- Enable tests and add extra dependencies
- Tests expect Debian host with grub-editenv, called grub2-editenv on Fedora

* Thu Apr 3 2025 Bruno Thomsen <bruno.thomsen@gmail.com> - 1.14-2
- Add patch that remove OpenSSL engine support

* Wed Apr 2 2025 Bruno Thomsen <bruno.thomsen@gmail.com> - 1.14-1
- Version bumped from 1.13 to 1.14
- Remove test failure comment from spec file

* Thu Mar 13 2025 Bruno Thomsen <bruno.thomsen@gmail.com> - 1.13-1
- Version bumped from 1.11.3 to 1.13

* Mon Feb 10 2025 Bruno Thomsen <bruno.thomsen@gmail.com> - 1.11.3-1
- Initial RPM release with test disabled as 6 fail and 17 ok
