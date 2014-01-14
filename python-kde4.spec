%define srcname pykde4

Summary:	KDE bindings to non-C++ languages
Name:		python-kde4
Version:	4.12.1
Release:	1
Epoch:		1
License:	GPLv2+
Group:		Development/KDE and Qt
Url:		http://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source:		ftp://ftp.kde.org/pub/kde/%{ftpdir}/%{version}/src/%{srcname}-%{version}.tar.xz
Patch0:		pykde4-4.10.0-respect-sip-flags.patch
# Revert commit that adds some python-sip-4.15 fixes and breaks older sip support
# https://bugs.kde.org/show_bug.cgi?id=325667
Patch1:		pykde4-4.11.2-sip4.15.patch
BuildRequires:	kdepimlibs4-devel
BuildRequires:	python-devel
BuildRequires:	python-qt4-devel >= 4.9
BuildRequires:	python-sip >= 1:4.14.0
# Seems to be broken for a long time
# BuildRequires:	pkgconfig(polkit-qt-1)
BuildRequires:	pkgconfig(shared-desktop-ontologies)
BuildRequires:	automoc4
Provides:	PyKDE4 = %{EVRD}
Provides:	pykde4 = %{EVRD}
Requires:	python-qt4 >= 4.9

%description
The Python bindings for KDE 4.

%files
%{py_platsitedir}/PyQt4/
%{py_platsitedir}/PyKDE4
%{_kde_bindir}/pykdeuic4*
%{_kde_libdir}/kde4/kpythonpluginfactory.so
%dir %{_kde_appsdir}/pykde4
%exclude %{_kde_datadir}/doc/python-kde4

#-----------------------------------------------------------------------------

%package devel
Summary:	PyKDE4 sip files and examples
Group:		Development/KDE and Qt
Requires:	python-kde4 = %{EVRD}
Requires:	python-qt4-devel

%description devel
Python KDE 4 sip files and examples.

%files devel
%{_kde_datadir}/sip/PyKDE4
%{_kde_appsdir}/pykde4/examples

#-----------------------------------------------------------------------------

%package doc
Summary:	PyKDE4 documentation
Group:		Development/KDE and Qt
BuildArch:	noarch

%description doc
Python bindings for KDE 4 documentation.

%files doc
%doc AUTHORS COPYING COPYING.LESSER NEWS README THANKS
%{_kde_datadir}/doc/python-kde4

#------------------------------------------------------------

%prep
%setup -q -n %{srcname}-%{version}
%patch0 -p1
SIPVER=$((`sip -V |cut -d. -f1` * 1000 + `sip -V |cut -d. -f2`))
if [ $SIPVER -lt 4015 ]; then
# This patch breaks sip 4.15, but restores working with versions before 4.15
%patch1 -p1
fi

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

# Copy Python Doc
mkdir -p %{buildroot}%{_kde_datadir}/doc/python-kde4
cp -a docs/html/* %{buildroot}%{_kde_datadir}/doc/python-kde4/

%changelog
* Tue Jan 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.1-1
- New version 4.12.1

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.3-1
- New version 4.11.3

* Wed Oct 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.2-2
- Add sip4.15 patch to revert some sip-4.15 fixes that break older sip support

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.0-1
- New version 4.11.0

* Fri Jul 19 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.5-2
- Update BuildRequires

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- New version 4.10.0
- Re-diff respect-sip-flags patch (bero)

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.1-1
- New version 4.9.1

* Sat Aug 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.0-1
- New version 4.9.0

* Thu Jul 12 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.97-1
- Update to 4.8.97
- Add pykde4-respect-sip-flags patch from Cooker

* Thu Jun 28 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.95-1
- Update to 4.8.95

* Wed Jun 20 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.90-1
- Update to 4.8.90
- Update BuildRequires (as it now requires python-sip 4.13.1+)

* Fri Jun 08 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 1:4.8.4-1
- update to 4.8.4

* Thu May 10 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 1:4.8.3-1
- update to 4.8.3

* Sun Mar 11 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 1:4.8.2-1
- update to 4.8.2

* Sun Mar 11 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 1:4.8.1-1
- update to 4.8.1

* Thu Jan 19 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.8.0-1
+ Revision: 762417
- New upstream tarball

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.97-1
+ Revision: 758118
- New upstream tarball

* Tue Jan 03 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.95-1
+ Revision: 748827
- Fix file list
- Fix file list
- Fix file list
- Fix file list
- New version

* Wed Dec 14 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.90-1
+ Revision: 740826
- New version

* Tue Nov 22 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.80-1
+ Revision: 732411
- Add Automoc4 as buildrequires ( to workaround a rpm5/iurt bug)
- New version 4.7.80

* Wed Sep 07 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.41-1
+ Revision: 698633
- imported package python-kde4

