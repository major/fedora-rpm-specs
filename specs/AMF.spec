Name:           AMF
Version:        1.4.35
Release:        3%{?dist}
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

%package        docs
Summary:        PDF documentation for %{name}

%description    docs
The %{name}-docs package contains the development documentation in PDF format
that is available in the main %{name}-devel package in Markdown format.


%prep
%autosetup -p1

%install
mkdir -p %{buildroot}%{_includedir}/%{name}
cp -fr amf/public/include/* %{buildroot}%{_includedir}/%{name}/

mkdir -p %{buildroot}%{_usrsrc}/%{name}
cp -fr amf/public/* %{buildroot}%{_usrsrc}/%{name}/
rm -fr %{buildroot}%{_usrsrc}/%{name}/include
ln -sf ../../include/AMF %{buildroot}%{_usrsrc}/%{name}/include

# Split out PDF docs
mkdir pdf
mv amf/doc/*pdf pdf/

%files devel
%license LICENSE.txt
%doc amf/doc/*
%{_includedir}/%{name}/

%files samples
%license LICENSE.txt
%{_usrsrc}/%{name}

%files docs
%license LICENSE.txt
%doc pdf/*

%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.35-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Oct 20 2024 Simone Caronni <negativo17@gmail.com> - 1.4.35-1
- Update to 1.4.35.
- Split out PDF docs.

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 03 2024 Simone Caronni <negativo17@gmail.com> - 1.4.34-1
- Update to 1.4.34.

* Mon Jan 29 2024 Simone Caronni <negativo17@gmail.com> - 1.4.33-1
- Update to 1.4.33.

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.32-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Dec 13 2023 Simone Caronni <negativo17@gmail.com> - 1.4.32-1
- Update to 1.4.32.

* Mon Aug 07 2023 Simone Caronni <negativo17@gmail.com> - 1.4.30-1
- Update to 1.4.30.

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
