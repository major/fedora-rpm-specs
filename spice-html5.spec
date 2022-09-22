Name:           spice-html5
Version:        0.3.0
Release:        5%{?dist}
Summary:        Pure Javascript SPICE client

License:        LGPLv3
URL:            http://www.spice-space.org
Source0:        https://gitlab.freedesktop.org/spice/spice-html5/-/archive/spice-html5-%{version}/spice-html5-spice-html5-%{version}.tar.bz2

BuildRequires:  make
BuildArch:      noarch

%description
%{name} is a Javascript SPICE client.  This includes a simple HTML
page to initiate a session, and the client itself.  It includes a configuration
file for Apache, but should work with any web server.

%prep
%setup -q -n spice-html5-spice-html5-%{version}


%build

%install
%make_install


%files
%{_datadir}/%{name}
%doc COPYING COPYING.LESSER README TODO apache.conf.sample


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 28 2020 Jeremy White <jwhite@codeweavers.com> - 0.3.0-1
- Release version 0.3.0
- New layout and look
- Improved audio support
- Implement as a module, to avoid namespace pollution
- Miscellaneous behavior improvements to mouse and keyboard

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 17 2016 Jeremy White <jwhite@codeweavers.com> 0.1.7-1
- Jeremy White: Add support for vp8 video streams
- Jeremy White: Support sized data streams and stream data reports
- Jeremy White: Add minor debug tools for media playback
- Jeremy White: Enable file transfer for spice_auto.html
- Oliver Gutierrez: avoid an unwanted exception when used by cockpit plugin
- Martin Hradil: Make spice_auto.html respect an input path
- Pavel Grunt: Minor Coverity adjustments
- Pavel Grunt: Improve log messages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar 13 2015 Jeremy White <jwhite@codeweavers.com> 0.1.6-1
- Pavel Grunt: Implement file transfer from client to guest
- Pavel Grunt: Report agent capabilities, handle agent tokens
- Pavel Grunt: Use WheelEvent instead of MouseWheelEvent
- Frantisek Kobzik: Improve error messages
- Report a modern number of tokens

* Thu Sep 25 2014 Jeremy White <jwhite@codeweavers.com> 0.1.5-1
- If an agent is attached, enable dynamic resizing of the guest screen.
- Add support for audio streams using the Opus encoding.
- Vladik Romanovsky: Use wss scheme when accessing with https protocol

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Sep 19 2013 Jeremy White <jwhite@codeweavers.com> 0.1.4-1
- Reduce memory leaks
- Ack every message.
- Aric Stewart: Fix and implement cache handling
- Jordan Pittier: Fix default websocket port detection in spice_auto.html
- Alon Levy: remove default password
- Thomas Goirand - Adds missing mapping of the alphanumeric minus key

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 23 2013 Jeremy White <jwhite@codeweavers.com> 0.1.3-1
- Correct spice_auto.html for a missing include for the spice array buffer.
- Provide limited compatibility for IE10.
- Amos Benari: added on succeess event and added sendCtrlAltDel method.

* Mon Feb 25 2013 Jeremy White <jwhite@codeweavers.com> 0.1.2-2
- Revise the .spec file to use %%{name}, and remove a few uneeded statements
- No longer install apache.conf, just put a sample under doc/
- Switch to an alternate download location, more easily updated

* Wed Feb 13 2013 Jeremy White <jwhite@codeweavers.com> 0.1.1-1
- Correct the license to LGPL
- Revise the Apache configuration file to allow access more broadly

* Fri Feb 8 2013 Jeremy White <jwhite@codeweavers.com> 0.1.0-1
- Initial version for packaging.
