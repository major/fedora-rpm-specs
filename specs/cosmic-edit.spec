# Generated using the scripts at https://pagure.io/fedora-cosmic/cosmic-packaging/blob/main/f/scripts
ExcludeArch: %{ix86}
# Generated by rust2rpm 26
%bcond_without check

%global crate cosmic-edit
%global build_rustflags %{?build_rustflags} --cfg=io_uring_skip_arch_check

# While our version corresponds to an upstream tag, we still need to define
# these macros in order to set the VERGEN_GIT_SHA and VERGEN_GIT_COMMIT_DATE
# environment variables in multiple sections of the spec file.
%global commit d4294713d8fc5c44ed7c9b1957aa6db7ee16a4d4
%global commitdatestring 2025-04-17 08:12:02 -0600
%global cosmic_minver 1.0.0~alpha.7

Name:           cosmic-edit
Version: 1.0.0~alpha.7
Release:        %autorelease
Summary:        Libcosmic text editor

License:        ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND (0BSD OR Apache-2.0 OR MIT) AND Apache-2.0 AND (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT) AND (Apache-2.0 OR BSD-2-Clause OR MIT) AND (Apache-2.0 OR BSD-3-Clause OR MIT) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR CC0-1.0 OR MIT) AND (Apache-2.0 OR CC0-1.0 OR MIT-0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR MIT OR Zlib) AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND CC0-1.0 AND GPL-2.0-only AND GPL-3.0-only AND ISC AND MIT AND (MIT OR Unlicense) AND MPL-2.0 AND Unicode-3.0 AND Zlib

URL:            https://github.com/pop-os/cosmic-edit

Source0:        https://github.com/pop-os/cosmic-edit/archive/epoch-%{version_no_tilde}/cosmic-edit-%{version_no_tilde}.tar.gz
# To create the below sources:
# * git clone https://github.com/pop-os/cosmic-edit at the specified commit
# * cargo vendor > vendor-config-%%{version_no_tilde}.toml
# * tar -pczf vendor-%%{version_no_tilde}.tar.gz vendor
Source1:        vendor-%{version_no_tilde}.tar.gz
# * mv vendor-config-%%{version_no_tilde}.toml ..
Source2:        vendor-config-%{version_no_tilde}.toml

BuildRequires:  cargo-rpm-macros >= 26
BuildRequires:  rustc
BuildRequires:  lld
BuildRequires:  cargo
BuildRequires:  just
BuildRequires:  libxkbcommon-devel
BuildRequires:  desktop-file-utils

Requires:       cosmic-icon-theme >= %{cosmic_minver}

%global _description %{expand:
%{summary}.}

%description %{_description}

%prep
%autosetup -n %{crate}-epoch-%{version_no_tilde} -p1 -a1
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
just rootdir=%{buildroot} prefix=%{_prefix} install

# COSMIC is not a valid category pre-fedora 41
%if %{defined fedora} && 0%{?fedora} < 41
desktop-file-install \
--remove-category COSMIC \
--add-category X-COSMIC \
--delete-original \
--dir %{buildroot}%{_datadir}/applications \
%{buildroot}%{_datadir}/applications/com.system76.CosmicEdit.desktop
%endif

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/com.system76.CosmicEdit.desktop
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
%doc README.md
%{_bindir}/cosmic-edit
%{_datadir}/applications/com.system76.CosmicEdit.desktop
%{_metainfodir}/com.system76.CosmicEdit.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/com.system76.CosmicEdit.svg

%changelog
%autochangelog
