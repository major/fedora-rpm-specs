Name:           R-V8
Version:        %R_rpm_version 8.0.1
Release:        %autorelease
Summary:        Embedded JavaScript and WebAssembly Engine for R

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}
Patch:          0001-Use-local-path-for-example-sources.patch

ExclusiveArch:  %{nodejs_arches}
BuildRequires:  R-devel
BuildRequires:  v8-devel
BuildRequires:  js-underscore
Requires:       js-underscore

# This is not packaged and it's only used to make sure example docs build when
# offline anyway.
Provides:       bundled(js-crossfilter) = 1.3.12

%description
An R interface to V8: Google's open source JavaScript and WebAssembly engine.

%prep
%autosetup -c -p1

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
