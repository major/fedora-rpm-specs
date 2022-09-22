Name:           gimp-fourier-plugin
Version:        0.4.3
Release:        %autorelease
Summary:        A simple plug-in to do fourier transform on your image

License:        GPL-3.0-or-later
URL:            https://www.lprp.fr/gimp_plugin_en/
Source0:        https://www.lprp.fr/files/old-web/soft/gimp/fourier-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(gimp-2.0)

BuildRequires:  dos2unix

Requires:       gimp

%description
A simple plug-in to do fourier transform on your image. The major advantage of 
this plugin is to be able to work with the transformed image inside GIMP.


%prep
%autosetup -n fourier-%{version}

# Remove pre-compiled executable
rm -vf fourier

for f in README README.Moire
do
  iconv --from-code=ISO-8859-1 --to-code=UTF-8 "${f}" > "${f}.tmp"
  dos2unix "${f}.tmp"
  touch -r "${f}" "${f}.tmp"
  mv "${f}.tmp" "${f}"
done


%build
%set_build_flags
# We must override the default CFLAGS/LIBS to respect distro flags (including
# ignoring the hard-coded -O2).
#
# We can’t use “gimptool-2.0 install-bin” to install into the buildroot.
# We therefore don’t need gimptool-2.0 at all.
%make_build \
    GIMPTOOL=/bin/false \
    GCC="${CC:-gcc}" \
    CFLAGS="${CFLAGS} $(pkgconf fftw3 gimp-2.0 --cflags)" \
    LIBS="${LDFLAGS} $(pkgconf fftw3 gimp-2.0 --libs) -lm"


%install
DESTDIR='%{buildroot}/%{_libdir}/gimp/2.0/plug-ins'
%make_install \
    GIMPTOOL=/bin/false \
    PLUGIN_INSTALL="install -t '${DESTDIR}' -D -p"


# Upstream provides no tests.


%files
%doc README
%doc README.Moire

%{_libdir}/gimp/2.0/plug-ins/fourier


%changelog
%autochangelog
