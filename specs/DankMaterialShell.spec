%global goipath github.com/AvengeMedia/%{name}/core

# Can't run tests in the network restricted buildenv
%bcond check 0

Name:           DankMaterialShell
Version:        1.2.3
Release:        5%{?dist}
Summary:        Desktop shell for Wayland compositors built on QuickShell

License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND GPL-3.0-only AND ISC AND MIT AND MPL-2.0
URL:            https://danklinux.com/
Source0:        https://github.com/AvengeMedia/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
%dnl dms-core go dependencies
%dnl Generated with the following:
%dnl $ tar xvf %{name}-%{version}.tar.bz2
%dnl $ cd %{name}-%{version}/core/
%dnl $ go_vendor_archive create %{name}-%{version}/core/ --output %{name}-%{version}-core-govendor.tar.bz2 --config %{S:2}
Source1:        %{name}-%{version}-core-govendor.tar.bz2
# Go Vendor Tools config
Source2:        go-vendor-tools.toml

# Fix screensaver inhibit support to fix anaconda crash
Patch0:         https://github.com/AvengeMedia/DankMaterialShell/commit/be8f3adf015c0cb02e520b8af455786caa78aa54.patch

BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools

BuildRequires:  systemd-rpm-macros

Requires:       accountsservice
Requires:       cups-pk-helper
Requires:       hicolor-icon-theme
Requires:       quickshell

Requires:       (adw-gtk3-theme if gtk3)
Requires:       cava
Requires:       cliphist
Requires:       danksearch
Requires:       dgop
Requires:       kf6-kimageformats
Requires:       khal
Requires:       matugen
Requires:       (qt5ct if qt5-qtbase)
Requires:       qt6ct
Requires:       qt6-qtmultimedia
Requires:       qt6-qtimageformats
Requires:       wl-clipboard

Recommends:     NetworkManager
Recommends:     ppd-service
Suggests:       tuned-ppd

# Replace and provide the package names from avengemedia/dms
Obsoletes:      dms < %{version}-%{release}
Provides:       dms = %{version}-%{release}
Obsoletes:      dms-cli < %{version}-%{release}
Provides:       dms-cli = %{version}-%{release}

%description
DankMaterialShell is a complete desktop shell for Wayland compositors.
It replaces a variety of tools used to stitch together to make a desktop.

It features notifications, an app launcher, wallpaper customization, and is
fully customizable with plugins.

It includes auto-theming for GTK/Qt apps with matugen, 20+ customizable widgets,
process monitoring, notification center, clipboard history, dock, control center,
lock screen, and comprehensive plugin system.


%prep
%autosetup -C -p1
tar -xf %{S:1} -C core


%generate_buildrequires
%go_vendor_license_buildrequires -c %{S:2}


%build
pushd core
export dms_buildtime=$(date -d "@${SOURCE_DATE_EPOCH}" +%%Y-%%m-%%d_%%H:%%M:%%S)
export GO_LDFLAGS="-X main.commit=fedora \
                   -X main.Version=%{version}-%{release} \
                   -X main.buildTime=${dms_buildtime}"
%global gomodulesmode GO111MODULE=on
mkdir -p %{_vpath_builddir}/bin
%gobuild -o %{_vpath_builddir}/bin/dms ./cmd/dms
popd


%install
# Install dms
install -Dm644 assets/systemd/dms.service %{buildroot}%{_userunitdir}/dms.service

install -Dm644 assets/dms-open.desktop %{buildroot}%{_datadir}/applications/dms-open.desktop
install -Dm644 assets/danklogo.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/danklogo.svg

mkdir -p %{buildroot}%{_datadir}/quickshell/dms
cp -a quickshell/* %{buildroot}%{_datadir}/quickshell/dms/
echo "%{version}-%{release}" > %{buildroot}%{_datadir}/quickshell/dms/VERSION


# Install dms cli
mkdir -p %{buildroot}%{_bindir}
install -pm0755 core/%{_vpath_builddir}/bin/dms %{buildroot}%{_bindir}/dms

# Install dms cli shell completions
mkdir -p %{buildroot}%{bash_completions_dir}
mkdir -p %{buildroot}%{fish_completions_dir}
mkdir -p %{buildroot}%{zsh_completions_dir}
core/%{_vpath_builddir}/bin/dms completion bash > %{buildroot}%{bash_completions_dir}/dms
core/%{_vpath_builddir}/bin/dms completion fish > %{buildroot}%{fish_completions_dir}/dms.fish
core/%{_vpath_builddir}/bin/dms completion zsh > %{buildroot}%{zsh_completions_dir}/_dms

pushd core
# Install dms cli licenses
%go_vendor_license_install -c %{S:2}
popd

%check
pushd core
# Not sure how to make this work properly...
%dnl %go_vendor_license_check -c %{S:2}
%if %{with check}
%gotest ./...
%endif
popd


%posttrans
# Signal running DMS instances to reload
pkill -USR1 -x dms || :


%files -f core/%{go_vendor_license_filelist}
%license LICENSE
%doc README.md
%{_bindir}/dms
%{bash_completions_dir}/dms
%{fish_completions_dir}/dms.fish
%{zsh_completions_dir}/_dms
%{_datadir}/quickshell/dms/
%{_userunitdir}/dms.service
%{_datadir}/applications/dms-open.desktop
%{_datadir}/icons/hicolor/scalable/apps/danklogo.svg

%changelog
* Mon Feb 16 2026 Neal Gompa <ngompa@fedoraproject.org> - 1.2.3-5
- Backport fix for screensaver inhibit support
- Add dependencies to make various wallpaper format work
- Add dependency for printer management support

* Mon Feb 16 2026 Neal Gompa <ngompa@fedoraproject.org> - 1.2.3-4
- Add missing khal dependency

* Mon Feb 16 2026 Neal Gompa <ngompa@fedoraproject.org> - 1.2.3-3
- Add dependency for ppd-service
- Fix string for embedded package version

* Sun Feb 15 2026 Neal Gompa <ngompa@fedoraproject.org> - 1.2.3-2
- Strengthen various dependencies

* Sun Feb 15 2026 Neal Gompa <ngompa@fedoraproject.org> - 1.2.3-1
- Initial package
