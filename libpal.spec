Name:           libpal
Version:        0.9.8
Release:        9%{?dist}
Summary:        Positional Astronomy Library

# The entire source is GPLv3+, except:
#
# LGPLv3+:
#   pal.h pal1sofa.h palmac.h
#
#   palAmpqk.c palDat.c palDe2h.c palDeuler.c palDh2e.c palDjcal.c
#   palDmat.c palDrange.c palDs2tp.c palDtp2s.c palDtps2c.c palDtt.c
#   palEcmat.c palEqgal.c palEtrms.c palEvp.c palFk45z.c palFk524.c
#   palFk54z.c palGaleq.c palGeoc.c palMappa.c palMapqkz.c palPrebn.c
#   palPrec.c palPrenut.c palPvobs.c palRvlg.c palRvlsrd.c palRvlsrk.c
#
# The effective license of the library and documenation is therefore
# GPLv3+, while the API headers are all LGPLv3+.
License:        GPLv3+
URL:            https://github.com/Starlink/pal
Source0:        https://github.com/Starlink/pal/releases/download/v%{version}/pal-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  erfa-devel

%description
The PAL library is a partial re-implementation of Pat Wallace's popular SLALIB
library written in C using a Gnu GPL license and layered on top of the IAU's
SOFA library (or the BSD-licensed ERFA) where appropriate. PAL attempts to
stick to the SLA C API where possible although palObs() has a more C-like API
than the equivalent slaObs() function. In most cases it is enough to simply
change the function prefix of a routine in order to link against PAL rather
than SLALIB. Routines calling SOFA use modern nutation and precession models
so will return slightly different answers than native SLALIB. PAL functions
not available in SOFA were ported from the Fortran version of SLALIB that
ships as part of the Starlink software and uses a GPL licence.


%package        devel
Summary:        Development files for %{name}
License:        LGPLv3+
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        doc
Summary:        Documentation for %{name}
License:        GPLv3+
BuildArch:      noarch

%description    doc
The %{name}-doc package contains documentation for %{name}.


%prep
%setup -q -n pal-%{version}


%build
%configure --disable-static --with-external_cminpack --with-external_pal
%make_build


%install
%make_install
find %{buildroot} -name '*.la' -delete
# Docs and licenses copied to strange places
rm -r %{buildroot}%{_prefix}/{manifests,news,share/pal}


%check
make check


%files
%license COPYING*
%doc README.md pal.news
%{_libdir}/libpal.so.0*

%files devel
# Directory is co-owned with ast-devel, which is related but not required
%dir %{_includedir}/star
%{_includedir}/star/pal*.h
%{_libdir}/libpal.so

%files doc
%license COPYING*
%doc sun267.pdf

%changelog
* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 12 2021 Orion Poplawski <orion@nwra.com> - 0.9.8-3
- Make doc noarch

* Thu Nov 11 2021 Orion Poplawski <orion@nwra.com> - 0.9.8-2
- Document licensing
- More explicit files
- Split out doc

* Fri Oct 29 2021 Orion Poplawski <orion@nwra.com> - 0.9.8-1
- Initial package
