Name:          piccata
Version:       2.0.1
Release:       2%{?dist}
Summary:       A simple Python based CoAP (RFC7252) toolkit
License:       MIT
URL:           https://github.com/NordicSemiconductor/piccata
Source0:       https://github.com/NordicSemiconductor/piccata/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Piccata is a simple CoAP (RFC7252) toolkit written in Python.

%package -n python3-piccata
Summary:        A simple Python based CoAP (RFC7252) toolkit

%description -n python3-piccata
Piccata is a simple CoAP (RFC7252) toolkit written in Python.

The toolkit provides basic building blocks for using CoAP in an application.
piccata handles messaging between endpoints (retransmission, deduplication)
and request/response matching.

Handling and matching resources, blockwise transfers, etc. is left to the
application but functions to faciliate this are provided.

Piccata uses a transport abstraction to faciliate using the toolkit for
communication over different link types. Transport for a UDP socket is provided.

%prep
%autosetup -p1

%build
%py3_build

%install
%py3_install

%files -n python3-piccata
%license LICENSE
%doc README.md
%{python3_sitelib}/piccata/
%{python3_sitelib}/transport/
%{python3_sitelib}/piccata-%{version}-py*.egg-info/

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Oct 18 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 2.0.1-1
- Initial Package
