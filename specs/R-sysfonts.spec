Name:           R-sysfonts
Version:        %R_rpm_version 0.8.9
Release:        %autorelease
Summary:        Loading Fonts into R

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  liberation-mono-fonts
BuildRequires:  liberation-sans-fonts
BuildRequires:  liberation-serif-fonts
Requires:       liberation-mono-fonts
Requires:       liberation-sans-fonts
Requires:       liberation-serif-fonts

%description
Loading system fonts and Google Fonts <https://fonts.google.com/> into R,
in order to support other packages such as 'R2SWF' and 'showtext'.

%prep
%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
# Replace fonts by system fonts (note that this cannot be done in prep because
# R CMD INSTALL copies symlink targets.)
pushd %{buildroot}%{_R_libdir}/sysfonts/fonts
rm AUTHORS License.txt
for family in Mono Sans Serif; do
    family_lower="${family,,}"
    for style in Regular Bold Italic BoldItalic; do
        rm Liberation${family}-${style}.ttf
        ln -s /usr/share/fonts/liberation-${family_lower}-fonts/Liberation${family}-${style}.ttf
    done
done
popd

%R_save_files

%check
%R_check

%files -f %{R_files}

%changelog
%autochangelog
