Name:           natural-earth-map-data
Version:        5.1.2
Release:        %autorelease
Summary:        Free vector and raster map data at 1:10m, 1:50m, and 1:110m scales

License:        Public Domain
URL:            https://www.naturalearthdata.com/
# Repackaged the zip as tar.xz because it saves a significant amount (~100MB).
# See repackage.sh.
#Source0:        https://naciscdn.org/naturalearth/{version}/110m/physical/110m_physical.zip#/110m_physical-{version}.zip
Source0:        110m_physical-%{version}.tar.xz
#Source1:        https://naciscdn.org/naturalearth/{version}/110m/cultural/110m_cultural.zip#/110m_cultural-{version}.zip
Source1:        110m_cultural-%{version}.tar.xz
#Source2:        https://naciscdn.org/naturalearth/{version}/50m/physical/50m_physical.zip#/50m_physical-{version}.zip
Source2:        50m_physical-%{version}.tar.xz
#Source3:        https://naciscdn.org/naturalearth/{version}/50m/cultural/50m_cultural.zip#/50m_cultural-{version}.zip
Source3:        50m_cultural-%{version}.tar.xz
#Source4:        https://naciscdn.org/naturalearth/{version}/10m/physical/10m_physical.zip#/10m_physical-{version}.zip
Source4:        10m_physical-%{version}.tar.xz
#Source5:        https://naciscdn.org/naturalearth/{version}/10m/cultural/10m_cultural.zip#/10m_cultural-{version}.zip
Source5:        10m_cultural-%{version}.tar.xz
Source6:        https://github.com/nvkelso/natural-earth-vector/raw/master/LICENSE.md
BuildArch:      noarch

%global _description \
Natural Earth is a public domain map dataset available at 1:10m, 1:50m, and \
1:110 million scales. Featuring tightly integrated vector and raster data, with \
Natural Earth you can make a variety of visually pleasing, well-crafted maps \
with cartography or GIS software.

%description %{_description}


%package        110m
Summary:        Natural Earth map data - 110m resolution

%description    110m %{_description}

This provides data at 1:110m resolution.


%package        50m
Summary:        Natural Earth map data - 50m resolution

%description    50m %{_description}

This provides data at 1:50m resolution.


%package        10m
Summary:        Natural Earth map data - 10m resolution

%description    10m %{_description}

This provides data at 1:10m resolution.


%package        all
Summary:        Natural Earth map data - all resolutions
Requires:       %{name}-110m
Requires:       %{name}-50m
Requires:       %{name}-10m

%description    all %{_description}

This provides data at all resolutions.


%prep
%setup -c -T
for scale in 110m 50m 10m; do
    mkdir ${scale}
    for theme in physical cultural; do
        mkdir ${scale}/${theme}
    done
done
# 110m
tar -C 110m/physical -xf %SOURCE0
tar -C 110m/cultural -xf %SOURCE1
# 50m
tar -C 50m/physical -xf %SOURCE2
tar -C 50m/cultural -xf %SOURCE3
# 10m
tar -C 10m/physical -xf %SOURCE4
tar -C 10m/cultural -xf %SOURCE5
# One has to be different...
mv 10m/cultural/10m_cultural/* 10m/cultural
rmdir 10m/cultural/10m_cultural
cp -p %SOURCE6 .


%install
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_pkgdocdir}
for theme in physical cultural; do
    mkdir -p %{buildroot}%{_datadir}/%{name}/${theme}
    for scale in 110m 50m 10m; do
        chmod -x ${scale}/${theme}/ne_${scale}_*
        cp -a ${scale}/${theme}/ne_${scale}_* %{buildroot}%{_datadir}/%{name}/${theme}
        for docfile in README.md CHANGELOG VERSION; do
            cp -a ${scale}/${theme}/${docfile} %{buildroot}%{_pkgdocdir}/${scale}-${theme}-${docfile}
        done
    done
done


%files 110m
%license LICENSE.md
%dir %{_pkgdocdir}
%{_pkgdocdir}/110m-*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/physical/
%{_datadir}/%{name}/physical/ne_110m_*
%dir %{_datadir}/%{name}/cultural/
%{_datadir}/%{name}/cultural/ne_110m_*


%files 50m
%license LICENSE.md
%dir %{_pkgdocdir}
%{_pkgdocdir}/50m-*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/physical/
%{_datadir}/%{name}/physical/ne_50m_*
%dir %{_datadir}/%{name}/cultural/
%{_datadir}/%{name}/cultural/ne_50m_*


%files 10m
%license LICENSE.md
%dir %{_pkgdocdir}
%{_pkgdocdir}/10m-*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/physical/
%{_datadir}/%{name}/physical/ne_10m_*
%dir %{_datadir}/%{name}/cultural/
%{_datadir}/%{name}/cultural/ne_10m_*


%changelog
%autochangelog
