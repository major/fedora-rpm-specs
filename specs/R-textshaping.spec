Name:           R-textshaping
Version:        %R_rpm_version 1.0.4
Release:        %autorelease
Summary:        Bindings to the HarfBuzz and Fribidi Libraries for Text Shaping

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(harfbuzz)
Obsoletes:      %{name}-devel <= 1.0.4

%description
Provides access to the text shaping functionality in the HarfBuzz library and
the bidirectional algorithm in the Fribidi library. textshaping is a low-level
utility package mainly for graphic devices that expands upon the font tool-set
provided by the systemfonts package.

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
