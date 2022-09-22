%global forgeurl https://github.com/antirez/%{name}
%global commit          de61bd564f1aa929bae414a70e421acd0b81789a

%forgemeta
Name:           dump1090
Version:        0
Release:        6%{?dist}
Summary:        Simple Mode S decoder specifically designed for RTLSDR devices

License:        BSD
URL:            %{forgeurl}
Source0:        %{forgesource}
# Man page
Source1:        dump1090.md
# Compressed "good" test output
Source2:	testoutput.gz
# Sometimes, analysis finds an additional 66 signals at the end
Source3:	testoutput2.gz
# Move data file gmap.html from current directory to /usr/share/dump1090
# so it will run out of the box for any user.
# There are many ways to run the daemon, and no obvious standard system service.
# https://github.com/antirez/dump1090/issues/163
Patch0:         dump1090-share.patch

BuildRequires:  gcc rtl-sdr-devel
BuildRequires:  pandoc

%description
Dump 1090 is a Mode S decoder specifically designed for RTLSDR devices.

Install this to use your RTL-SDR to track commercial aircraft in your area.

The main features are:

* Robust decoding of weak messages, with mode1090 many users observed
  improved range compared to other popular decoders.
* Network support: TCP30003 stream (MSG5...), Raw packets, HTTP.
* Embedded HTTP server that displays the currently detected aircraft on
  Google Map.
* Single bit errors correction using the 24 bit CRC.
* Ability to decode DF11, DF17 messages.
* Ability to decode DF formats like DF0, DF4, DF5, DF16, DF20 and DF21
  where the checksum is xored with the ICAO address by brute forcing the
  checksum field using recently seen ICAO addresses.
* Decode raw IQ samples from file (using --ifile command line switch).
* Interactive command-line interface mode where aircraft currently detected
  are shown as a list refreshing as more data arrives.
* CPR coordinates decoding and track calculation from velocity.
* TCP server streaming and receiving raw data to/from connected clients
  (using --net).

%prep
%forgeautosetup
# Extract LICENSE from source
# https://github.com/antirez/dump1090/issues/164
sed -ne 's/^ \*//' -e '/Copyright/,/DAMAGE\./p' anet.h >LICENSE
pandoc -s -tman -o %{name}.1 %{SOURCE1}
zcat %{SOURCE2} >testoutput
zcat %{SOURCE2} %{SOURCE3} >testoutput2

%build
%set_build_flags
%make_build 

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}
install -pm 755 dump1090  %{buildroot}%{_bindir}
install -pm 644 gmap.html  %{buildroot}%{_datadir}/%{name}
cp -pr tools  %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_mandir}/man1
install -pm 644 %{name}.1 %{buildroot}%{_mandir}/man1

%check
./dump1090 --ifile testfiles/modes1.bin >testout
diff testout testoutput || diff testout testoutput2

%files
%license LICENSE
%doc README.md TODO
%{_bindir}/dump1090
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1.gz

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 11 2021 Stuart D. Gathman <stuart@gathman.org> 0-4.20210727gitde61bd5
- Add markdown man page

* Wed Aug  4 2021 Stuart D. Gathman <stuart@gathman.org> 0-3.20210727gitde61bd5
- Minor formatting nits

* Mon Aug  2 2021 Stuart D. Gathman <stuart@gathman.org> 0-2.20210727gitde61bd5
- Link to issue for patch
- use %%set_build_flags macro
- use %%forge macros
- extract LICENSE from anet.h
- fix perms on gmap.html

* Tue Jul 27 2021 Stuart D. Gathman <stuart@gathman.org> 0-1.20210727gitde61bd5
- Initial RPM
