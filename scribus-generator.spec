#Versioning for scribus
#%%global versioning 1.5.3.svn/
Name:		scribus-generator
Version:	3.0
Release:	%autorelease
Summary:	Open source high-quality PDF template and mail-merge alternative

License:	MIT
URL:		https://github.com/berteh/ScribusGenerator

Source0:	https://github.com/berteh/ScribusGenerator/archive/%{version}.tar.gz#/ScribusGenerator-%{version}.tar.gz
Source1:	%{name}.metainfo.xml

BuildRequires:	libappstream-glib
BuildRequires:	pkgconfig(python3)
Requires:	python3-tkinter
Requires:	scribus

BuildArch:	noarch

%description
Mail-Merge-like extension to Scribus, to generate Scribus and 
PDF documents automatically from external data.

%prep
%autosetup -n ScribusGenerator-%{version}

# Fix all Python shebangs recursively in .
%py3_shebang_fix .

%build
#Nothing to builds

%install
install -Dpm 0644 *.{py,conf} -t %{buildroot}%{_datadir}/scribus/scripts/
chmod +x %{buildroot}%{_datadir}/scribus/scripts/*.py
cp -r {example,pic} %{buildroot}%{_datadir}/scribus/scripts/


# Add AppStream metadata
install -Dm 0644 -p %{SOURCE1} \
	%{buildroot}%{_metainfodir}/%{name}.metainfo.xml

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

%files
%license LICENSE
%doc README.md
%{_datadir}/scribus/scripts/*
#AppStream metadata
%{_metainfodir}/%{name}.metainfo.xml


%changelog
%autochangelog
