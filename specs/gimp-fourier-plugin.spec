Name:           gimp-fourier-plugin
Version:        0.4.5+gimp3rc1
%global srcversion %{gsub %{version} + -}
Release:        %autorelease
Summary:        Do direct and reverse Fourier Transforms on your image

License:        GPL-3.0-or-later
URL:            https://www.lprp.fr/gimp_plugin_en/
%global forgeurl https://github.com/rpeyron/plugin-gimp-fourier
Source:         %{forgeurl}/archive/v%{version}/plugin-gimp-fourier-%{srcversion}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
#
# The gimp package dropped s390x support in
# https://src.fedoraproject.org/rpms/gimp/c/778e871c1051ea063ce679b18ae84f0a3c47b6f7.
# Per the tracking bug https://bugzilla.redhat.com/show_bug.cgi?id=2318369,
# there is no upstream support in the gimp project for big-endian
# architectures, so this ExcludeArch is likely to be permanent.
ExcludeArch:    %{ix86} s390x

BuildRequires:  gcc
BuildRequires:  make

BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool

BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(gimp-3.0)

BuildRequires:  dos2unix

# Minimum version for plugin API/ABI compatibility
Requires:       gimp%{?_isa} >= 2:3.0.0~RC1

%description
GIMP Plugin to do forward and reverse Fourier Transform. The major advantage of
this plugin is to be able to work with the transformed image inside GIMP. You
can draw or apply filters in fourier space and get the modified image with an
inverse fourier transform. Useful in fixing moire patterns or fixing some
regular banding noise.


%prep
%autosetup -n plugin-gimp-fourier-%{srcversion} -p1
dos2unix --keepdate README.md


%conf
autoreconf --force --install --verbose
%configure --enable-gimp3-fourier


%build
%make_build


%install
%make_install
%find_lang gimp30-fourier


# Upstream provides no tests.


%files -f gimp30-fourier.lang
%license LICENSE
%doc README.md
%doc README.Moire

%{_libdir}/gimp/3.0/plug-ins/fourier


%changelog
%autochangelog
