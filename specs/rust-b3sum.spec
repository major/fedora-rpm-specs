# Generated by rust2rpm 27
%bcond check 1

%global crate b3sum

Name:           rust-b3sum
Version:        1.8.2
Release:        %autorelease
Summary:        Command line implementation of the BLAKE3 hash function

License:        Apache-2.0 OR Apache-2.0 WITH LLVM-exception
URL:            https://crates.io/crates/b3sum
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * Remove CC0-1.0 option (not allowed for code in Fedora) from license
#   expression (but note that LICENSE still includes CC0-1.0 text); see
#   https://docs.fedoraproject.org/en-US/legal/spdx/#_spdx_license_expressions_in_fedora_license_data
Patch:          b3sum-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  help2man

%global _description %{expand:
A command line implementation of the BLAKE3 hash function.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# Apache-2.0 OR Apache-2.0 WITH LLVM-exception
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause
# MIT
# MIT OR Apache-2.0
# MIT-0 OR Apache-2.0
License:        %{shrink:
                (Apache-2.0 OR MIT) AND
                (Apache-2.0 WITH LLVM-exception OR Apache-2.0) AND
                (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
                BSD-2-Clause AND
                MIT AND
                (MIT-0 OR Apache-2.0)
                }
# LICENSE.dependencies contains a full license breakdown

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE_A2
%license LICENSE_A2LLVM
%license LICENSE.dependencies
%doc README.md
%doc what_does_check_do.md
%{_bindir}/b3sum
%{_mandir}/man1/b3sum.1*

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
help2man --no-info --output=b3sum.1 target/rpm/b3sum

%install
%cargo_install
install -t %{buildroot}%{_mandir}/man1 -D -p -m 0644 b3sum.1

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
