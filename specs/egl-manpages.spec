%global forgeurl https://github.com/KhronosGroup/EGL-Registry
%global commit 8e56e86e65687697ef54114cdb1afabdfac756bf
%forgemeta

Name:           egl-manpages
Version:        1.5
Release:        %autorelease
Summary:        EGL API man pages

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        metainfo.xsl

BuildArch:      noarch

BuildRequires:  libxslt
BuildRequires:  docbook5-style-xsl

%description
Man pages for the EGL API, the Khronos Native Platform Graphics Interface.
EGL provides mechanisms for creating rendering surfaces and contexts for
client APIs such as OpenGL ES and OpenVG, and for synchronizing drawing
across APIs and native platform rendering.

%prep
%forgesetup

%build
pushd sdk/docs/man
    for MANP in egl*.xml ; do
        xsltproc --xinclude --nonet %{SOURCE1} $MANP | \
            xsltproc --xinclude --nonet /usr/share/sgml/docbook/xsl-ns-stylesheets/manpages/docbook.xsl -
    done
popd

%install
mkdir -p %{buildroot}%{_mandir}/man3/
cp -a sdk/docs/man/*.3G %{buildroot}%{_mandir}/man3/

%files
%license sdk/docs/man/copyright.xml
%{_mandir}/man3/*

%changelog
%autochangelog
