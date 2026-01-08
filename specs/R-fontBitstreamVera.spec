Name:           R-fontBitstreamVera
Version:        %R_rpm_version 0.1.1
Release:        %autorelease
Summary:        Fonts with 'Bitstream Vera Fonts' License

License:        Bitstream-Vera
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel
BuildRequires:  bitstream-vera-fonts-all
Requires:       bitstream-vera-fonts-all

%description
Provides fonts licensed under the 'Bitstream Vera Fonts' license for the
'fontquiver' package.

%prep
%autosetup -c
# Ensure we are replacing fonts by the same system fonts later.
grep ttf fontBitstreamVera/MD5 | grep -v 'Mo\|Se' | sed -e 's!*inst!/usr/share!' -e 's!-fonts!-sans-fonts!' | md5sum -c
grep ttf fontBitstreamVera/MD5 | grep 'Mo' | sed -e 's!*inst!/usr/share!' -e 's!-fonts!-sans-mono-fonts!' | md5sum -c
grep ttf fontBitstreamVera/MD5 | grep 'Se' | sed -e 's!*inst!/usr/share!' -e 's!-fonts!-serif-fonts!' | md5sum -c
# We don't provide woffs.
rm fontBitstreamVera/inst/fonts/bitstream-vera-fonts/*.woff
sed -i -e '/woff/d' fontBitstreamVera/MD5
# Remove bunfled Bitstream files that are not important for this package.
rm fontBitstreamVera/inst/fonts/{bitstream-vera-VERSION,Makefile}
rm fontBitstreamVera/inst/fonts/bitstream-vera-fonts/{*.TXT,local.conf}
sed -i -e '/Makefile/d' -e '/VERSION/d' -e '/TXT/d' -e '/local.conf/d' fontBitstreamVera/MD5

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
# Replace fonts by system fonts (note that this cannot be done in prep because
# R CMD INSTALL copies symlink targets.)
for f in Vera VeraBd VeraIt VeraBI; do
    rm %{buildroot}%{_R_libdir}/fontBitstreamVera/fonts/bitstream-vera-fonts/$f.ttf
    ln -s /usr/share/fonts/bitstream-vera-sans-fonts/$f.ttf %{buildroot}%{_R_libdir}/fontBitstreamVera/fonts/bitstream-vera-fonts/$f.ttf
done
for f in VeraMono VeraMoBd VeraMoIt VeraMoBI; do
    rm %{buildroot}%{_R_libdir}/fontBitstreamVera/fonts/bitstream-vera-fonts/$f.ttf
    ln -s /usr/share/fonts/bitstream-vera-sans-mono-fonts/$f.ttf %{buildroot}%{_R_libdir}/fontBitstreamVera/fonts/bitstream-vera-fonts/$f.ttf
done
for f in VeraSe VeraSeBd; do
    rm %{buildroot}%{_R_libdir}/fontBitstreamVera/fonts/bitstream-vera-fonts/$f.ttf
    ln -s /usr/share/fonts/bitstream-vera-serif-fonts/$f.ttf %{buildroot}%{_R_libdir}/fontBitstreamVera/fonts/bitstream-vera-fonts/$f.ttf
done

%R_save_files

%check
%R_check

%files -f %{R_files}

%changelog
%autochangelog
