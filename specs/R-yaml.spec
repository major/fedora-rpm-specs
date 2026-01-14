Name:           R-yaml
Version:        %R_rpm_version 2.3.12
Release:        %autorelease
Summary:        Methods to Convert R Data to YAML and Back

# See `COPYING` for license breakdown.
License:        BSD-3-Clause AND MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

# Slightly patched, so can't unbundle yet.
Provides:       bundled(libyaml) = 0.2.5

%description
Implements the 'libyaml' 'YAML' 1.1 parser and emitter
(<https://pyyaml.org/wiki/LibYAML>) for R.

%prep
%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check

%files -f %{R_files}

%changelog
%autochangelog
