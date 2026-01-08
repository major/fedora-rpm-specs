Name:           R-fontLiberation
Version:        %R_rpm_version 0.1.0
Release:        %autorelease
Summary:        Liberation Fonts

# Automatically converted from old format: OFL - review is highly recommended.
License:        LicenseRef-Callaway-OFL
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel
BuildRequires:  liberation-sans-fonts >= 2.00.1
BuildRequires:  liberation-mono-fonts >= 2.00.1
BuildRequires:  liberation-serif-fonts >= 2.00.1
Requires:       liberation-sans-fonts >= 2.00.1
Requires:       liberation-mono-fonts >= 2.00.1
Requires:       liberation-serif-fonts >= 2.00.1

%description
A placeholder for the Liberation fontset intended for the `fontquiver` package.
This fontset covers the 12 combinations of families (sans, serif, mono) and
faces (plain, bold, italic, bold italic) supported in R graphics devices.

%prep
%autosetup -c

# We don't ship woffs.
rm fontLiberation/inst/fonts/liberation-fonts/*.woff
# Remove useless files
rm fontLiberation/inst/fonts/{liberation-VERSION,Makefile}
rm fontLiberation/inst/fonts/liberation-fonts/{AUTHORS,ChangeLog,LICENSE,README,TODO}
sed -i -e '/VERSION/d' -e '/Makefile/d' -e '/liberation-fonts\//d' fontLiberation/MD5

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install

# Replace fonts by system fonts (note that this cannot be done in prep because
# R CMD INSTALL copies symlink targets.)
for f in %{buildroot}%{_R_libdir}/fontLiberation/fonts/liberation-fonts/*.ttf; do
    rm $f
    ln -s /usr/share/fonts/liberation/${f##*/} $f
done

%R_save_files

%check
%R_check

%files -f %{R_files}

%changelog
%autochangelog
