Name:           krun-awsnitro-eif-ctl
Version:        0.1.0
Release:        %autorelease
Summary:        EIF configuration tool for krun-awsnitro

# Apache-2.0
# Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
# Unlicense OR MIT
License:        %{shrink:
    Apache-2.0 AND
    MIT AND
    (Apache-2.0 OR MIT) AND
    (Unlicense OR MIT)
    }
URL:            https://github.com/virtee/krun-awsnitro-eif-ctl
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cargo-rpm-macros >= 24

%description
Tool to configure cached EIF files for the krun-awsnitro runtime for AWS
Nitro Enclaves

%prep
%autosetup -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires -t

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
%cargo_install

%check
%cargo_test

%files
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/krun-awsnitro-eif-ctl

%changelog
%autochangelog
