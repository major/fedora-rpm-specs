Name:           R-clisymbols
Version:        %R_rpm_version 1.2.0
Release:        %autorelease
Summary:        Unicode Symbols at the R Prompt

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
A small subset of Unicode symbols, that are useful when building command line
applications. They fall back to alternatives on terminals that do not support
Unicode. Many symbols were taken from the 'figures' 'npm' package (see
<https://github.com/sindresorhus/figures>).

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
