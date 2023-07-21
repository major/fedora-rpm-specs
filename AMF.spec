Name:           AMF
Version:        1.4.29
Release:        2%{?dist}
Summary:        Advanced Media Framework (AMF) SDK
License:        MIT
URL:            https://gpuopen.com/advanced-media-framework/
BuildArch:      noarch

# Cleaned up tarballi without Thirdparty folder:
Source0:        %{name}-cleaned-%{version}.tar.gz
Source1:        %{name}-tarball.sh

%description
A light-weight, portable multimedia framework that abstracts away most of the
platform and API-specific details. %{name} is supported on the closed source AMD
Pro driver and OpenMax on the open source AMD Mesa driver.

%package        devel
Summary:        Development files for %{name}

%description    devel
A light-weight, portable multimedia framework that abstracts away most of the
platform and API-specific details. %{name} is supported on the closed source AMD
Pro driver and OpenMax on the open source AMD Mesa driver.

The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package        samples
Summary:        Sample files for %{name}

%description    samples
The %{name}-samples package contains sample programs and source for applications
that use %{name}.

%prep
%autosetup -p1

%install
mkdir -p %{buildroot}%{_includedir}/%{name}
cp -fr amf/public/include/* %{buildroot}%{_includedir}/%{name}/

mkdir -p %{buildroot}%{_usrsrc}/%{name}
cp -fr amf/public/* %{buildroot}%{_usrsrc}/%{name}/
rm -fr %{buildroot}%{_usrsrc}/%{name}/include
ln -sf ../../include/AMF %{buildroot}%{_usrsrc}/%{name}/include

%files devel
%license LICENSE.txt
%doc amf/doc/*
%{_includedir}/%{name}/

%files samples
%{_usrsrc}/%{name}

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Feb 04 2023 Simone Caronni <negativo17@gmail.com> - 1.4.29-1
- Update to 1.4.29.

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Oct 09 2022 Simone Caronni <negativo17@gmail.com> - 1.4.26-1
- Update to 1.4.26.

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Apr 07 2022 Simone Caronni <negativo17@gmail.com> - 1.4.24-1
- Update to 1.4.24.

* Sun Feb 13 2022 Simone Caronni <negativo17@gmail.com> - 1.4.23-2
- Remove Thirdparty folder from sources and provide script to recreate tarball.
- Remove duplicated docs in samples subpackage.

* Thu Feb 10 2022 Simone Caronni <negativo17@gmail.com> - 1.4.23-1
- First build.
