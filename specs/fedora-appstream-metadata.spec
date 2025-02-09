Summary:        Operating System AppStream Metadata for Fedora Linux
Name:           fedora-appstream-metadata
# Use the time of the last metadata update as version
Version:        20250207
Release:        %autorelease
License:        MIT
URL:            https://fedoraproject.org/
Source1:        org.fedoraproject.fedora.metainfo.xml
Source2:        LICENSE
Source3:        update-appstream-metadata.go
BuildArch:      noarch

%description
Operating System AppStream Metadata for Fedora Linux

%prep
# only appstream 1.0 knows about "snapshot" releases
%if 0%{?fedora} < 40
sed -i '/<release / s/type="snapshot"/type="development"/' %{SOURCE1}
%endif

%build

%install
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_datadir}/metainfo/org.fedoraproject.fedora.metainfo.xml
install -Dpm 0644 %{SOURCE2} %{buildroot}%{_datadir}/licenses/%{name}/LICENSE

%files
%license LICENSE
%{_datadir}/metainfo/org.fedoraproject.fedora.metainfo.xml

%changelog
%autochangelog
