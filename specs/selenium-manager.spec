%global cargo_install_lib 0

Name:           selenium-manager
Version:        4.34.0
Release:        %autorelease
Summary:        Automated driver and browser management for Selenium
# Full break down of the licenses is located in the LICENCE.dependencies file.
# Result of cargo_license_summary:
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0
# Apache-2.0 AND ISC AND (MIT OR Apache-2.0)
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR ISC OR MIT
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-3-Clause
# CDLA-Permissive-2.0
# ISC
# MIT
# MIT OR Apache-2.0
# MIT OR Zlib OR Apache-2.0
# MPL-2.0
# Unicode-3.0
# Unlicense OR MIT
# bzip2-1.0.6


# The code in directory /rust is under the Apache-2.0 licence.
# The rest of the code under other licences is not shipped or used for the built built.
License:        %{shrink:
                Apache-2.0 AND
                BSD-3-Clause AND
                CDLA-Permissive-2.0 AND
                ISC AND
                MIT AND
                MPL-2.0 AND
                Unicode-3.0 AND
                Unicode-DFS-2016 AND
                bzip2-1.0.6 AND
                (0BSD OR MIT OR Apache-2.0) AND
                (Apache-2.0 OR BSL-1.0) AND
                (Apache-2.0 OR ISC OR MIT) AND
                (Apache-2.0 OR MIT) AND
                (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
                (MIT OR Apache-2.0 OR Zlib) AND
                (Unlicense OR MIT)
                }

URL:            https://github.com/SeleniumHQ/selenium
Source0:        %{url}/archive/selenium-%{version}.tar.gz

# Patches remove the requirements to pull dependencies
# used by other OS or linux distributions.
# For example apple-flat-package or debpkg,
# doesn't have representation in fedora repo and shoudn't be used.
# Corresponding funcitons using these dependencies then also have to be deleted.
# Issue is based on lack of target configuration when building from source.
# Upstream status: https://github.com/SeleniumHQ/selenium/issues/15009#issuecomment-3027302387
Patch0:         0001-remove-unnecessary-dependencies.patch
Patch1:         0001-remove-unsupported-function.patch

BuildRequires:  cargo-rpm-macros >= 24

%description
Selenium Manager is a command-line tool implemented in Rust
that provides automated driver and browser management for Selenium.

%prep
%autosetup -n selenium-selenium-%{version}/rust/ -N
%patch -P 0 
cd src
%patch -P 1 
cd ..
%cargo_prep 

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
%cargo_install

%files
%license ../LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/selenium-manager

%changelog
%autochangelog

