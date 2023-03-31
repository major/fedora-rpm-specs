Name:          zanata-python-client
Version:       1.5.3
Release:       15%{?dist}
Summary:       Python3 Client for Zanata Server
License:       LGPL-2.0-or-later
URL:           http://zanata.org
Source0:       https://github.com/zanata/zanata-python-client/archive/v%{version}.tar.gz

BuildArch:     noarch
BuildRequires: python3-setuptools
BuildRequires: python3-devel

%global _description\
Zanata Python client is a client that communicate with Zanata server.

%description %_description

%package -n python3-zanata-client
Summary:       %summary
Requires:      python3dist(polib)
Requires:      python3dist(httplib2)
Requires:      python3dist(lxml)
Requires:      python3dist(future)
%{?python_provide:%python_provide python3-zanata-client}

%description -n python3-zanata-client %_description

%prep
%autosetup

%build
%py3_build
cp -pr zanataclient/VERSION-FILE build/lib/zanataclient

%install
%py3_install

# Let the docdir be by name python3-zanata-client
rm -rf $RPM_BUILD_ROOT/%{_docdir}

%files -n python3-zanata-client
%doc README.rst zanata.ini zanata_example.xml CHANGELOG
%license COPYING.LESSER
%{_bindir}/flies
%{_bindir}/zanata
%{python3_sitelib}/zanataclient
%{python3_sitelib}/zanata_python_client-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Mar 29 2023 Sundeep Anand <suanand@redhat.com> - 1.5.3-15
- update license tag to as per SPDX identifiers

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.5.3-12
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.5.3-9
- Rebuilt for Python 3.10

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.3-6
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.3-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.3-3
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 07 2019 Parag Nemade <pnemade AT fedoraproject DOT org> - 1.5.3-1
- Update to 1.5.3 release

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 04 2018 Parag Nemade <pnemade AT fedoraproject DOT org> - 1.5.2-2
- Update to follow latest packaging guidelines

* Mon Apr 16 2018 Sundeep Anand <suanand@redhat.com> - 1.5.2-1
- Upstream update to 1.5.2-1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.5.1-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sun Dec 17 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.5.1-4
- Python 2 binary package renamed to python2-zanata-client
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 26 2016 Sundeep Anand <suanand@redhat.com> - 1.5.1-1
- Upstream update to 1.5.1-1

* Fri Apr 15 2016 Sundeep Anand <suanand@redhat.com> - 1.5.0-2
- add build requires, v1.5.0 release notes:
  - Bug 1139950 - Translation files mapping rules
  - Bug 1311705 - traceback when trying to push
  - ZNTA-303 - podir projects handling
  - ZNTA-927 - Project Status and Versions
  - ZNTA-929 - failed to retrieve version in non-git environment
  - ZNTA-934 - init failed to generate java-client compatible zanata.xml
  - ZNTA-936 - error message for unexpected html response
  - ZNTA-946 - Cannot push with zanata Python client 1.4.2

* Fri Apr 15 2016 Ding-Yi Chen <dchen@redhat.com> - 1.5.0-1
- Upstream update to 1.5.0-1

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 21 2016 Ding-Yi Chen <dchen@redhat.com> - 1.4.2-1
- Upstream update to 1.4.2

* Wed Jan 20 2016 Jason L Tibbitts III <tibbs@math.uh.edu> - 1.4.1-4
- Change define -> global to fix build issue with epel-rpm-macros.

* Thu Jan 14 2016 Ding-Yi Chen <dchen@redhat.com> - 1.4.1-3
Fix the EPEL5 build.

* Thu Jan 14 2016 Ding-Yi Chen <dchen@redhat.com> - 1.4.1-2
- Fix the Fedora 22 rpmlint error.

* Wed Jan 13 2016 Ding-Yi Chen <dchen@redhat.com> - 1.4.1-1
- Upsteam update to 1.4.1 which fixed:
  * Improvements
    - zanata init Initialize Zanata project configuration
    - zanata stats Displays translation statistics for a Zanata project version
  * Bug fixes
    - Bug 1206995 - Should allow anonymous pull from Zanata
    - Bug ZNTA-853 - Crash when pushing local translations

* Thu Dec 10 2015 Ding-Yi Chen <dchen@redhat.com> - 1.4.0-1
- Upsteam update to 1.4.0 which fixed:
  - Bug 1215274 - specify minimum percentage completion on pull
  - Rename zanatalib/project.py to zanatalib/projectutils.py
  - Bug 1156236 - use locale aliases defined in the server
  - added ProjectContext, Improved help, fixed code issues
  - added <src-dir> and <trans-dir> in zanata.xml
  - refactor code - added config to centralize rest resources
  - Organize exception messages, added test.
  - HTTP to HTTPS redirect - auto, if found in httplib2 response
  - Rename zanatalib/client.py to zanatalib/resource.py
  - flake8 changes and addition of: make flake8
  - added requirements.txt

* Mon Jul 27 2015 Anish Patil <anish.developer@gmail.com> - 1.3.22-1
- Upstream has released new version

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 03 2015 Anish Patil <apatil@redhat.com> - 1.3.21-1
- Upstream has released new version

* Mon Mar 02 2015 Anish Patil <apatil@redhat.com> - 1.3.20-1
- Upstream has released new version

* Mon Feb 23 2015 Anish Patil <apatil@redhat.com> - 1.3.19-1
- Upstream has released new version

* Wed Dec 03 2014 Anish Patil <apatil@redhat.com> - 1.3.18-1
- Upstream has released new version

* Thu Nov 06 2014 Anish Patil <apatil@redhat.com> - 1.3.16-2
- New package guidelines,removed doc dir at the end of install

* Fri Sep 19 2014 Anish Patil <apatil@redhat.com> - 1.3.16-1
- Upstream has released new version

* Fri Jul 25 2014 Anish Patil <apatil@redhat.com> - 1.3.15-1
- Incorporated package review comments

* Thu Jul 24 2014 Anish Patil <apatil@redhat.com> - 1.3.14-2
- Incorporated package review comments

* Tue Jul 22 2014 Anish Patil <apatil@redhat.com> - 1.3.14-1
- Upstream has released new version

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Nov 21 2012 Sean Flanigan <sflaniga@redhat.com> - 1.3.13-1
- Use dict instead of nested loop
- Ensure that msgstr_plural is always set for plural strings
- Rename message to poentry for consistency

* Thu Nov 15 2012 Sean Flanigan <sflaniga@redhat.com> - 1.3.12-1
- Revised test files
- Use PUT instead of POST/PUT when pushing source documents
- Change Flies to Zanata in messages

* Tue Aug 07 2012 Ding-Yi Chen <dchen@redhat.com> - 1.3.11-1
- Updated: CHANGELOG and setup.py

* Tue Aug 07 2012 Ding-Yi Chen <dchen@redhat.com> - 1.3.10-1
- Fixed rhbz#727833, "Copy previous translations:True" is ambiguous

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 James Ni <jni@redhat.com> - 1.3.8-1
- Fix issue of po/publican push and po/publican pull command for project_type
- Fixed rhbz826821, glossary-push failed on big compendium po file
- Add link of trouble shooting page to error message
- Fix bypass ssl certificate check issue
- Change Delete to Deleting

* Wed Jun 13 2012 James Ni <jni@redhat.com> - 1.3.7-1
- Fixed rhbz#827316, failed to push pot with msgid_plural against 1.6 server
- Fixed rhbz#826798, zanata pull fail to pull
- Fixed rhbz#814593, "TypeError: 'unicode' object does not support item assignment" when pulling translation from server
- Fixed rhbz#820046, Python client generates empty msgctxt "" when pushing
- Fixed rhbz#795643, Python client pushes extracted comments instead of translator comments
- Fix the query param of skeletons
- Add option --disable-ssl-cert to python client
- Add help message for noskeletons option in pull, change content of Error 403
- Fixed the query param of skeletons
- Implment --push-type option, omit --push-trans when specify --push-type option
- Implement glossary delete command
- Refactoring code and remove duplicate code

* Thu Apr 26 2012 James Ni <jni@redhat.com> - 1.3.5-1
- Fixed rhbz#814593, "TypeError: 'unicode' object does not support item assignment" when pulling translation from server
- Part of rhbz#736898, implement push-trans-only option in python client so that user can do offline translation
- Fixed rhbz#814503, backtrace for zanata glossary push without "zanata.xml"
- Fixed rhbz#798084, Python client does not show helpful error when missing project id for 'project info' command
- Fixed rhbz#796039, Python client not recognizing source directories with pot files only in sub-directories.
- Fixed rhbz#795643, Python client pushes extracted comments instead of translator comments
- Fixed rhbz#744277, output more informative error message for unescaped quote
- Add msgid_plural and msgstr_plural support in python client (for server >=1.6)
- Add skeletons query parameter support in pull command
- Replace the address of FSF in license
- Add status code to error message

* Tue Feb 21 2012 James Ni <jni@redhat.com> - 1.3.4-1
- Fixed rhbz#795237: zanata python client still display depreciate help on "version create"
- Fixed rhbz#727386: zanata po push does not assume working directory
- Fixed rhbz#754869: The python client is pulling some files with a wrong path
- Fixed rhbz#768877: python client breaks PO file when no translation found
- Fixed rhbz#748727: US31 As a translator I want the appropriate character encoding for my language to be used so that
                     the content is saved in the correct encoding format
- Add warning for retired project/version

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 01 2011 James Ni <jni@redhat.com> - 1.3.3-1
- Fixed rhbz#751648: Error reading path names with dots
- Fixed rhbz#754869: The python client is pulling some files with a wrong path
- Fixed rhbz#756617: python client process file name not correctly for file name contain more than one dot
- Fixed rhbz#753719: Python client explodes on F16

* Thu Nov 03 2011 James Ni <jni@redhat.com> - 1.3.2-1
- csv format glossary file support
- support msgctxt when pushing po file to server and pull it back
- Fixed rhbz#696474: python client should only delete files from server which no longer exist on client
- Fixed rhbz#690687: python client should log a message for 301 redirects
- Fixed rhbz#738510: --help does not list commands
- Fixed rhbz#740159: python client: pushing with --merge=import does not overwrite the translation on server
- Fixed rhbz#738907: can not disable copytrans option when pushing source to zanata server with --no-copytrans option
- Fixed rhbz#738514: zanata push fails with JSON error
- Fixed rhbz#750675: zanata client pull command should be able to reconstruct msgctxt and msgid

* Wed Aug 31 2011 James Ni <jni@redhat.com> - 1.3.1-1
- Fix #rhbz734270 Reinstate publican/po push '--import-po' option

* Tue Aug 23 2011 James Ni <jni@redhat.com> - 1.3.0-1
- Change to version 1.3.0

* Wed Jul 20 2011 James Ni <jni@redhat.com> - 1.2.6-1
- Change to version 1.2.6

* Thu Jun 02 2011 James Ni <jni@redhat.com> - 1.2.5-3
- Fix error of onditionals of RHEL5

* Thu Jun 02 2011 James Ni <jni@redhat.com> - 1.2.5-2
- Add python-simplejson requires for RHEL5

* Wed Jun 01 2011 James Ni <jni@redhat.com> - 1.2.5-1
- Bug fix and usability improvement

* Thu May 05 2011 James Ni <jni@redhat.com> - 1.2.4-1
- Fix rhbz#702192

* Wed Apr 27 2011 James Ni <jni@redhat.com> - 1.2.3-1
- Fix rhbz#696474, rhbz#696515, rhbz#696437, rhbz#698028, rhbz#695598, rhbz#690687

* Fri Apr 01 2011 James Ni <jni@redhat.com> - 1.2.2-1
- Change to version 1.2.2

* Thu Mar 31 2011 James Ni <jni@redhat.com> - 1.2.1-2
- Fixed rpmlint: W: self-obsoletion flies-python-client < 1.3 obsoletes flies-python-client = 1.2.1-1.el6

* Thu Mar 31 2011 James Ni <jni@redhat.com> - 1.2.1-1
- Add flies command for fallback

* Thu Mar 31 2011 James Ni <jni@redhat.com> - 1.2.0-2
- Change the URL, add Provides and Obsoletes, add zanata.ini in %%doc

* Tue Mar 29 2011 James Ni <jni@redhat.com> - 1.2.0-1
- Rename the flies to zanata, rename fliesclient to zanataclient

* Thu Mar 10 2011 James Ni <jni@redhat.com> - 0.8.1-1
- Fix bugs(issue 272, issue 274) of retrieve the translation

* Mon Mar 07 2011 James Ni <jni@redhat.com> - 0.8.0-1
- Stable release

* Wed Feb 23 2011 James Ni <jni@redhat.com> - 0.7.6-1
- Rename the command line option, add a Logger class for better output, set copytrans default value to true, make the
  extensions to a list of gettext and comment.

* Tue Feb 22 2011 James Ni <jni@redhat.com> - 0.7.4-1
- Fix issue 245:stop processing when type 'n', Add version service, rename the command line option and help info, add
  InternalServerError

* Mon Feb 21 2011 James Ni <jni@redhat.com> - 0.7.3-1
- Fix issue 244, issue 245, issue 247 and issue 30, add command list for 'flies publican', rewrite the README

* Fri Feb 18 2011 James Ni <jni@redhat.com> - 0.7.2-1
- Rename the gettextutil to publicanutil, Remove the translator from textFlowTarget, Add more help info

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 24 2011 James Ni <jni@redhat.com> - 0.7.1-1
- Fix typo and make help more user-friendly

* Mon Jan 24 2011 James Ni <jni@redhat.com> - 0.7.0-1
- Add copyTrans option to client

* Tue Jan 04 2011 James Ni <jni@redhat.com> - 0.6.1-1
- Add exception handler for empty extensions

* Wed Dec 29 2010 James Ni <jni@redhat.com> - 0.6.0-1
- Create pot file with content retrieved from server, user could choose keep or delete the content on the flies
  server when pushing publican

* Tue Dec 07 2010 James Ni <jni@redhat.com> - 0.5.1-1
- Fix bugs and add some log info for python client

* Thu Dec 02 2010 James Ni <jni@redhat.com> - 0.5.0-1
- Make the script compatible with python 2.4

* Mon Nov 29 2010 James Ni <jni@redhat.com> - 0.4.0-1
- Add command line option for translation folder and importPo, read and write multiple locale, read the flies.xml first

* Wed Oct 27 2010 James Ni <jni@redhat.com> - 0.3.2-1
- Fix a typo in project creation

* Fri Oct 22 2010 James Ni <jni@redhat.com> - 0.3.1-1
- Fix an issue in project creation

* Thu Oct 21 2010 James Ni <jni@redhat.com> - 0.3.0-1
- Fix the issues in extension support and update translation command

* Thu Oct 21 2010 James Ni <jni@redhat.com> - 0.2.0-1
- Add extension support and update translation command

* Wed Sep 29 2010 James Ni <jni@redhat.com> - 0.1.0-1
- Modify the user configuration file and command line options

* Wed Sep 08 2010 James Ni <jni@redhat.com> - 0.0.6-1
- Try to resolve the dependency of python-setuptools

* Mon Sep 06 2010 James Ni <jni@redhat.com> - 0.0.5-2
- Add requires for python-polib

* Tue Aug 31 2010 James Ni <jni@redhat.com> - 0.0.5-1
- Rename resservice in flieslib/__init__.py to docservice

* Mon Aug 30 2010 James Ni <jni@redhat.com> - 0.0.4-1
- Rename module resservice to docservice
- Set encode to UTF-8 when generate hash value for msgid of the po file
- Change functions in flies.py to private
- Fix a exception in projectservice and exception handler in flies
- Provide more "readable" output for httplib2 connection error

* Wed Aug 25 2010 James Ni <jni@redhat.com> - 0.0.3-3
- Add an error handler for list command
- Add cache to httplib2

* Mon Aug 23 2010 James Ni <jni@redhat.com> - 0.0.3-2
- Include the example configuration file
- Add dependency of python-httplib2 for fedora 12(and less)

* Fri Aug 20 2010 James Ni <jni@redhat.com> - 0.0.3-1
- Modify the __inin__.py for importing the module
- Modify the spec file and fliesrc.txt
- Rewrite README file for giving detail of commands and how to implement flies-python-lib in program
- Add COPYING.LESSER

* Mon Aug 16 2010 James Ni <jni@redhat.com> - 0.0.2-2
- remove shebang from flies.py

* Fri Aug 13 2010 James Ni <jni@redhat.com> - 0.0.2-1
- initial package (#623871)
