%define		_class		Pager
%define		upstream_name	%{_class}

Name:		php-pear-%{upstream_name}
Version:	2.4.8
Release:	6
Summary:	Generic data paging class
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Pager/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Provides:	pear(Pager/Wrapper.php)
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
Obsoletes:	php-pear-Pager_Sliding
BuildArch:	noarch
BuildRequires:	php-pear

%description
If you have data that needs paging (ie 1-10 on page one, 11-20 on page
two) this class can help. Pass it an array of data and it will sort it
into pages, picking up the current page id from the url. It can also
give you back/next and page number links taking the current url and
adding the correct page id to it.


%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/examples
%{_datadir}/pear/%{_class}
%{_datadir}/pear/%{_class}.php
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 2.4.8-5mdv2012.0
+ Revision: 742261
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 2.4.8-4
+ Revision: 679566
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 2.4.8-3mdv2011.0
+ Revision: 613758
- the mass rebuild of 2010.1 packages

* Sat Nov 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.4.8-2mdv2010.1
+ Revision: 467940
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Sun Jun 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.4.8-1mdv2010.0
+ Revision: 383556
- update to new version 2.4.8

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 2.4.7-2mdv2009.1
+ Revision: 322654
- rebuild

* Sun Oct 12 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.4.7-1mdv2009.1
+ Revision: 292887
- update to new version 2.4.7

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 2.4.3-2mdv2009.0
+ Revision: 237054
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 2.4.3-1mdv2008.1
+ Revision: 136415
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 2.4.3-1mdv2008.0
+ Revision: 15743
- 2.4.3


* Sat Sep 23 2006 David Walluck <walluck@mandriva.org> 2.4.1-2mdv2007.0
- Pager_Wrapper.php is required by some applications
- Provides: php-pear-Pager_Sliding

* Sat May 20 2006 Oden Eriksson <oeriksson@mandriva.com> 2.4.1-1mdk
- 2.4.1

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 2.3.6-1mdk
- 2.3.6
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 2.3.3-4mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 2.3.3-3mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 2.3.3-2mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 2.3.3-1mdk
- 2.3.3

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 2.3.1-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 2.3.1-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 2.3.1-1mdk
- initial Mandriva package (PLD import)

