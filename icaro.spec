%global  __os_install_post %{nil}
%if 0%{?fedora} >= 25
%global activity TurtleBlocks.activity
%else
%global activity TurtleArt.activity
%endif

%global commit 7e5dca818e86870158292a1b212a1171129fed65
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name: icaro
Version: 2.0
Release: 11%{?dist}
Summary: Robotic Educational Project
# Icaro is licensed under GPLv3
# Pinguino and puf is licensend under LGPLv2
License: GPLv3 and LGPLv2
URL:		http://roboticaro.org
Source0:	https://github.com/valentinbasel/icaro/archive/%{commit}.tar.gz

# Add README in english
Source1:	README.ENG
BuildArch:	noarch
ExclusiveArch: %{ix86} x86_64 noarch
ExcludeArch:   s390 s390x ppc arm

BuildRequires:	desktop-file-utils
#BuildRequires:	sugar-toolkit

#Requires:	pygtksourceview
Requires:	sdcc
Requires:	gputils
#Requires:	sugar-turtleart
#Requires:	sugar
Requires:	vte

%description
An educational robotic software aimed to develop robotic 
and programming fundamentals.

%prep
%autosetup

# sugar-turtleart change paths
#%if 0%{?fedora} >= 18
#sed -i -e 's/TurtleArt.activity/TurtleBlocks.activity/' config.dat 
#%endif


# copy README.ENG file to sources as well.
#cp -a %{SOURCE1} .

#empty files
#echo "# Just a comment" > pic16/np05/tmp/stdout

# fix spurious permissions in this files
#chmod -v 0644 README.md COPYING AUTHORS COPYING-LGPLv2
chmod -v 0644 COPYING AUTHORS COPYING-LGPLv2


%build
#Nothing to build

%install
# ------------- Apicaro -------------------------------------

#{__python3} apicaro/setup.py install --root %{buildroot}


# ------------- Icaro ---------------------------------------
mkdir -p %{buildroot}%{_datadir}/%{name}/

cp -p -a  {hardware,imagenes,ejemplos,locale,clemente} %{buildroot}%{_datadir}/%{name}/
install -p -m 0644 {*.py,version} %{buildroot}%{_datadir}/%{name}/

# Remove po and pot files
find %{buildroot} -name "*.po" | xargs rm -f
find %{buildroot} -name "*.pot" | xargs rm -f
find %{buildroot} -name "#template.pde#" | xargs rm -f


%find_lang %{name}

# Tortucaro plugin for sugar
# NO more
#mkdir -p %{buildroot}%{sugaractivitydir}/%{activity}/plugins/icaro/
#cp -a plugintortucaro/icaro/* %{buildroot}%{sugaractivitydir}/%{activity}/plugins/icaro/
#mkdir -p %{buildroot}%{sugaractivitydir}/%{activity}/plugins/icaro/icons
#cp -a plugintortucaro/icaro/icons/* %{buildroot}%{sugaractivitydir}/%{activity}/plugins/icaro/icons
#mkdir -p %{buildroot}%{sugaractivitydir}/%{activity}/plugins/icaro/libreria
#cp -a plugintortucaro/icaro/libreria/*%{buildroot}%{sugaractivitydir}/%{activity}/plugins/icaro/libreria

mkdir -p %{buildroot}%{_sysconfdir}/udev/rules.d/
install -p -m 0644  udev/* %{buildroot}%{_sysconfdir}/udev/rules.d/

mkdir -p %{buildroot}%{_bindir}


#create executable of program
cat > icaro <<EOF
#! /bin/bash
python /usr/share/icaro/main.py
EOF

install -p -m 0755 icaro %{buildroot}%{_bindir}/%{name}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/

# Icon 
install -p -D -m 0644 imagenes/icarologo.png  %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/

#create desktop file
desktop-file-install \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

SAVEIFS=$IFS
IFS=$(echo -en "\n\b")
# Changes permissions files (with spaces in the filenames)
for file in `find %{buildroot}/%{_datadir}/%{name} -type f  -perm /a+x `; do
    chmod -v a-x $file
done

# Delete backup files (with spaces in the filenames)
for file in `find %{buildroot}%{_datadir}/%{name} -type f  -name '*~'`; do
    rm -rf $file
done
IFS=$SAVEIFS


for file in `find %{buildroot}%{_datadir}/%{name} -type f  ! -perm /a+x -name '*.py'`; do
    chmod -vR a+x $file
done

for file in `find %{buildroot}/%{python_sitelib}/%{name} -type f  ! -perm /a+x -name '*.py'`; do
    chmod -vR a+x $file
done

#for file in `find %{buildroot}/%{python_sitelib}/apicaro -type f  ! -perm /a+x -name '*.py'`; do
#    chmod -vR a+x $file
#done

find %{buildroot}%{_datadir}/%{name} -name '__init__.py' | xargs chmod 0644



%files -f %{name}.lang
%doc COPYING AUTHORS COPYING-LGPLv2 
#README.ENG 
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/*.py*
%{_datadir}/%{name}/version
%dir %{_datadir}/%{name}/hardware/icaro/v4/imagenes/componentes
%{_datadir}/%{name}/hardware/icaro/v4/imagenes/componentes/*
# Samples and Demos complex
%dir %{_datadir}/%{name}/ejemplos
%{_datadir}/%{name}/ejemplos/*


#Imagenes
%dir %{_datadir}/%{name}/imagenes
%{_datadir}/%{name}/imagenes/*

%dir %{_datadir}/%{name}/clemente
%{_datadir}/%{name}/clemente/*.py

%dir %{_datadir}/%{name}/imagenes/main
%{_datadir}/%{name}/imagenes/main/*.png

%dir %{_datadir}/%{name}/imagenes/mouse
%{_datadir}/%{name}/imagenes/mouse/*.*

%dir %{_datadir}/%{name}/hardware/icaro/
%{_datadir}/%{name}/hardware/icaro/*


#Samples by Firmware
%dir %{_datadir}/%{name}/hardware/icaro/v4/ejemplos
%{_datadir}/%{name}/hardware/icaro/v4/ejemplos/*


# Pinguino Firmware
# Exception granted by fpc
# For more details, see https://fedorahosted.org/fpc/ticket/253

#Copyng images files
%dir %{_datadir}/%{name}/hardware/icaro/v4/micro/firmware/pic16
%dir %{_datadir}/%{name}/hardware/icaro/v4/micro/firmware/pic16/lib
%{_datadir}/%{name}/hardware/icaro/v4/imagenes/componentes/*.png

%{_datadir}/%{name}/hardware/icaro/v4/imagenes/gif/*.gif
%{_datadir}/%{name}/hardware/icaro/v4/imagenes/*.png

# rpmlint complains for this file. arch-independent-package-contains-binary-or-object error
# Really not intended as a file for be executed in Fedora host.

%{_datadir}/%{name}/hardware/icaro/v4/micro/firmware/icaro_lib/*.h
%{_datadir}/%{name}/hardware/icaro/v4/micro/firmware/icaro_lib/*.c

%{_datadir}/%{name}/hardware/icaro/v4/micro/firmware/source/pilas/*.c

%{_datadir}/%{name}/hardware/icaro/v4/micro/firmware/source/tortucaro/*.c
%{_datadir}/%{name}/hardware/icaro/v4/micro/firmware/source/icaroblue/*.c


%{_datadir}/%{name}/hardware/icaro/v4/*.py

%{_datadir}/%{name}/hardware/*.py
%{_datadir}/%{name}/hardware/icaro/v4/modulos/*.py
%{_datadir}/%{name}/hardware/icaro/v4/micro/conf/*.ini


%{_datadir}/%{name}/hardware/icaro/v4/micro/firmware/pic16/lkr/*.lkr
%dir %{_datadir}/%{name}/hardware/icaro/v4/micro/firmware/icaro_lib
%dir %{_datadir}/%{name}/hardware/icaro/v4/micro/firmware/source
%{_datadir}/%{name}/hardware/icaro/v4/micro/firmware/source/*.c
%{_datadir}/%{name}/hardware/icaro/v4/micro/firmware/source/*.pde

%dir %{_datadir}/%{name}/hardware/icaro/v4/micro/firmware/non-free/include/pic16
%{_datadir}/%{name}/hardware/icaro/v4/micro/firmware/non-free/include/pic16/*.h

%dir %{_datadir}/%{name}/hardware/icaro/v4/micro/firmware/non-free/lib/pic16
%{_datadir}/%{name}/hardware/icaro/v4/micro/firmware/non-free/lib/pic16/*.lib

%dir %{_datadir}/%{name}/hardware/icaro/v4/micro/firmware/tmp
%{_datadir}/%{name}/hardware/icaro/v4/micro/firmware/tmp/*.c
%{_datadir}/%{name}/hardware/icaro/v4/micro/firmware/tmp/*.h

%dir %{_datadir}/%{name}/hardware/icaro/v4/micro/firmware/tmp/usb
%{_datadir}/%{name}/hardware/icaro/v4/micro/firmware/tmp/usb/*.c
%{_datadir}/%{name}/hardware/icaro/v4/micro/firmware/tmp/usb/*.h

%{_datadir}/%{name}/hardware/icaro/v4/micro/firmware/temporal/
%{_datadir}/%{name}/hardware/icaro/v4/micro/firmware/tmp/stdout

%dir %{_datadir}/%{name}/hardware/icaro/v4/micro/firmware/pic16/obj
%{_datadir}/%{name}/hardware/icaro/v4/micro/firmware/pic16/obj/*.o


%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop

#esto daba error, parece ser del menu 
%{_datadir}/icons/hicolor/48x48/apps/icarologo.png


%config(noreplace) %{_sysconfdir}/udev/rules.d/icaro.rules

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 24 2019 Omar Berroteran <omarberroteranlkf@gmail.com> - 2.0
- Remove python2 dependencies
- Improve and bug fixes
- remove sugar dependencies


* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 01 2018 Omar Berroteran <omarberroteranlkf@gmail.com> - 1.0.9
- Changes to Apicaro to improve stability.
- Changes all uDev to icaro.rules
- Add new Blocks
- Add Samples
- Remove Obsolete scritplets
- Changes Tortucaro
- Bump to the new upstream version (April 10, 2017)
- rebuilt

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.8-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.8-5
- Remove obsolete scriptlets

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Apr 13 2017 Omar Berroteran <omarberroteranlkf@gmail.com> - 1.0.8-3
- Changes to Apicaro to improve stability on BootLoader v4 de Pingüino.
- Set the BootLoader v4 to default.

* Thu Apr 13 2017 Omar Berroteran <omarberroteranlkf@gmail.com> - 1.0.8
- Bump to the new upstream version (April 10, 2017)
- Remove pyWebKit dependence because fedora 26  compatibility
- most bugfixes, improbe performance
- new firmwares and boot options
- Icaro Plugins changes 

* Sat Nov 12 2016 Omar Berroteran <omarberroteranlkf@gmail.com> - 1.0.7
- Bump to the new upstream version

* Wed Sep 28 2016 Omar Berroteran <omarberroteranlkf@gmail.com> - 1.0.6
- Bump to the new upstream version
- Firmware Tortucaro set pause time to 10
- se resetea el pic. ahora tiene una espera de 20 seg donde prende y apaga el led1 y con eso estabiliza la comunicación entre el pic y la pc
- 

* Mon Sep 26 2016 Dominik Mierzejewski <rpm@greysector.net> - 1.0.5-3
- rebuilt for matplotlib-2.0.0

* Tue Aug 23 2016 Omar Berroteran <omarberroteranlkf@gmail.com> -1.0.5-2
+  Requires:	python-matplotlib

* Wed Jul 20 2016 Omar Berroteran <omarberroteranlkf@gmail.com> -1.0.4-4
- Bump to the new upstream version
- changes on Apicaro

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jan 10 2015 Eduardo Echeverria <echevemaster@gmail.com>  - 1.0.4-1
- Bump to the new upstream version

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Nov 08 2013 Eduardo Echeverria <echevemaster@gmail.com>  - 1.0.3-1
- Bump to the new upstream version

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 8 2013 Eduardo Echeverria <echevemaster@gmail.com> - 1.0.2-2
- Fix issues with paths

* Sat Jun 8 2013 Eduardo Echeverria <echevemaster@gmail.com> - 1.0.2-1
- Updated to the new upstream version 1.0.2
- Switch from pygame to pycairo

* Sat Mar 30 2013 Eduardo Echeverria <echevemaster@gmail.com> - 1.0.1-1
- Updated to the new upstream version

* Sat Mar 09 2013 Eduardo Echeverria <echevemaster@gmail.com> - 1.0-3
- Added license LGPLv2 for the firmware
- Add missing requires
- Improve find_lang

* Wed Dec 12 2012 Eduardo Echeverria <echevemaster@gmail.com> - 1.0-2
- Add support to languages
- Add scriplets for icons
- Create executables for icaro
- Fix permissions
- Clean spec

* Fri Sep 28 2012 Yader Velasquez <yaderv@fedoraproject.org> - 1.0-1
- First Initial Packaging
