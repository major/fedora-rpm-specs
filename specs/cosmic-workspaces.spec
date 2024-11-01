ExcludeArch: %{ix86}
# Generated by rust2rpm 26
%bcond_without check


%global crate cosmic-workspaces


%global commit 70d6c415a1cd931f575c3e18274c3fecc7cc9a03
%global shortcommit %{sub %{commit} 1 7}
%global commitdatestring 2024-08-07 15:01:26 -0700
%global commitdate 20240807

Name:           cosmic-workspaces
Version:        1.0.0~alpha.2
Release:        %autorelease
Summary:        Workspaces overview for the COSMIC Desktop Environment

License:        CC0-1.0 AND (MIT OR Zlib OR Apache-2.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (Unlicense OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (MIT OR Apache-2.0 OR Zlib) AND MPL-2.0 AND Unicode-3.0 AND MIT AND (Zlib OR Apache-2.0 OR MIT) AND BSD-2-Clause AND (MIT OR Apache-2.0 OR CC0-1.0) AND ISC AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND BSD-3-Clause AND BSL-1.0 AND (MIT OR Apache-2.0) AND Apache-2.0 AND (0BSD OR MIT OR Apache-2.0) AND Zlib

URL:            https://github.com/pop-os/cosmic-workspaces-epoch

Source0:        https://github.com/pop-os/cosmic-workspaces-epoch/archive/%{commit}/cosmic-workspaces-epoch-%{shortcommit}.tar.gz
# To create the below sources:
# * git clone https://github.com/pop-os/cosmic-workspaces-epoch at the specified commit
# * cargo vendor > vendor-config-%%{shortcommit}.toml
# * tar -pczf vendor-%%{shortcommit}.tar.gz vendor
Source1:        vendor-%{shortcommit}.tar.gz
# * mv vendor-config-%%{shortcommit}.toml ..
Source2:        vendor-config-%{shortcommit}.toml


BuildRequires:  cargo-rpm-macros >= 26
BuildRequires:  rustc
BuildRequires:  lld
BuildRequires:  cargo
BuildRequires:  wayland-devel
BuildRequires:  systemd-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  libglvnd-devel
BuildRequires:  libseat-devel
BuildRequires:  libinput-devel
BuildRequires:  mesa-libgbm-devel
BuildRequires:  make
BuildRequires:  desktop-file-utils

Requires:       cosmic-comp
Requires:       hicolor-icon-theme

%global _description %{expand:
%{summary}.}

%description %{_description}

%prep
%autosetup -n cosmic-workspaces-epoch-%{commit} -p1 -a1
%cargo_prep -N
# Check if .cargo/config.toml exists
if [ -f .cargo/config.toml ]; then
  # If it exists, append the contents of %%{SOURCE2} to .cargo/config.toml
  cat %{SOURCE2} >> .cargo/config.toml
  echo "Appended %{SOURCE2} to .cargo/config.toml"
else
  # If it does not exist, append the contents of %%{SOURCE2} to .cargo/config
  cat %{SOURCE2} >> .cargo/config
  echo "Appended %{SOURCE2} to .cargo/config"
fi

%build
# Set vergen environment variables
export VERGEN_GIT_COMMIT_DATE="date --utc '%{commitdatestring}'"
export VERGEN_GIT_SHA="%{commit}"
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}
sed 's/\(.*\) (.*#\(.*\))/\1+git\2/' -i cargo-vendor.txt

%install
# Set vergen environment variables
export VERGEN_GIT_COMMIT_DATE="date --utc '%{commitdatestring}'"
export VERGEN_GIT_SHA="%{commit}"
make install DESTDIR=%{buildroot} prefix=%{_prefix}

# COSMIC is not a valid category pre-fedora 41
%if %{defined fedora} && 0%{?fedora} < 41
desktop-file-install \
--remove-category COSMIC \
--add-category X-COSMIC \
--delete-original \
--dir %{buildroot}%{_datadir}/applications \
%{buildroot}%{_datadir}/applications/com.system76.CosmicWorkspaces.desktop
%endif

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/com.system76.CosmicWorkspaces.desktop
%if %{with check}
# Set vergen environment variables
export VERGEN_GIT_COMMIT_DATE="date --utc '%{commitdatestring}'"
export VERGEN_GIT_SHA="%{commit}"
%cargo_test
%endif

%files
%license LICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%{_bindir}/cosmic-workspaces
%{_datadir}/applications/com.system76.CosmicWorkspaces.desktop
%{_datadir}/icons/hicolor/scalable/apps/com.system76.CosmicWorkspaces.svg

%changelog
%autochangelog
